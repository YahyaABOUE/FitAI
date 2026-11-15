# FitAI – AI Fitness Coach

## Description
FitAI is an intelligent fitness assistant that generates personalized workout plans based on the user's profile (age, goals, fitness level and physical constraints).

The project combines a Python backend API, AI techniques (embeddings) and a Neo4j graph database to produce consistent recommendations tailored to each user.

## Main Features
- User profile creation
- Automatic workout plan generation
- Exercises adapted to fitness level and goals
- Clear separation between backend and frontend

## Tech Stack
**Backend:**
- Python 3
- FastAPI
- Neo4j (graph database)
- OpenAI API (embeddings and reasoning)
- Uvicorn

**Frontend:**
- HTML
- CSS
- JavaScript

## Installation & Usage

1. **Clone the project**
   ```bash
   git clone https://github.com/YahyaABOUE/FitAI.git
   cd FitAI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - Linux / macOS: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r backend/app/requirements.txt
   ```

4. **Set environment variables**

   Create a `.env` file in `backend/app` with:
   ```
   OPENAI_API_KEY=your_openai_key
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_password
   ```

5. **Run the backend**
   ```bash
   cd backend/app
   uvicorn main:app --reload
   ```
   The API will be available at http://127.0.0.1:8000

6. **Run the frontend**

   Open `frontend/index.html` in a web browser.

## Academic Purpose
This project was built in an academic setting to demonstrate:
- The use of a modern backend API (FastAPI)
- The integration of AI into a real-world application
- The use of a graph database (Neo4j)
- A clean, modular software architecture

## Authors
- Yahya ABOU EL AZIZ
- Mehdi GUELLIDA
- Younes EL MAJDOUBI EL IDRISSI
- Khalil KASIMI

## License
Project built for educational purposes.
