import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from models import UserProfile, PlanResponse
from neo4j_client import Neo4jClient
from embeddings_service import semantic_match
from prompt_template import PROMPT
from openai import OpenAI
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

load_dotenv()

app = FastAPI(title="AI Fitness Coach - Prototype")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
neo = Neo4jClient()

CANONICAL_GOALS = ["Build Muscle", "Lose Fat", "Improve Endurance", "Conditioning"]
CANONICAL_EXPERIENCE = ["Beginner", "Intermediate", "Advanced"]


@app.post("/plan", response_model=PlanResponse)
async def create_plan(profile: UserProfile):

    best_goal, _ = semantic_match(profile.goal, CANONICAL_GOALS, top_k=1)[0]
    best_exp, _ = semantic_match(profile.experience, CANONICAL_EXPERIENCE, top_k=1)[0]

    exercises = neo.get_filtered_exercises(
        goal=best_goal,
        equipment=profile.equipment or [],
        injuries=profile.injuries or [],
        experience=best_exp
    )

    if not exercises:
        raise HTTPException(status_code=404, detail="No suitable exercises found for this profile")

    user_json = profile.dict()


    final_prompt = PROMPT.format(
        user=json.dumps(user_json, indent=2),
        exercises=json.dumps(exercises, indent=2),
        days=profile.days_per_week
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content":
                        "You are an AI fitness planner. "
                        "Return ONLY valid JSON. No explanation. "
                        "Format: { summary: str, week: {} }"
                },
                {"role": "user", "content": final_prompt},
            ],
            temperature=0.2,
            max_tokens=1000
        )

        raw = response.choices[0].message.content
        print("\n===== RAW OUTPUT =====\n", raw, "\n=====================\n")

        plan = json.loads(raw)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {e}")

    return PlanResponse(
        summary=plan.get("summary", ""),
        week=plan.get("week", {})
    )

@app.post("/export-pdf")
async def export_pdf(data: dict):

    summary = data.get("summary", "")
    week = data.get("week", {})

    pdf_path = "workout_plan.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Your AI-Generated Workout Plan")
    y -= 40

    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Summary:")
    y -= 20

    text_obj = c.beginText(50, y)
    text_obj.setFont("Helvetica", 11)
    for line in summary.split("\n"):
        text_obj.textLine(line)
    c.drawText(text_obj)

    y = text_obj.getY() - 30

    for day, exercises in week.items():
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, day.upper())
        y -= 25

        c.setFont("Helvetica", 11)
        for ex in exercises:
            block = f"{ex['name']}  |  Sets: {ex['sets']}  |  Reps: {ex['reps']}"
            c.drawString(50, y, block)
            y -= 18

            if "notes" in ex:
                c.setFillColorRGB(0.4, 0.4, 0.4)
                c.drawString(60, y, f"Notes: {ex['notes']}")
                c.setFillColorRGB(0, 0, 0)
                y -= 18

        y -= 20

        if y < 100:
            c.showPage()
            y = height - 50

    c.save()
    return FileResponse(pdf_path, filename="workout_plan.pdf")


@app.on_event("shutdown")
def shutdown():
    neo.close()
