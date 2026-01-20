from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "test1234")  # your password


# ===========================
# BIG EXERCISE DATASET — CHUNK 1
# ===========================
seed_data = {
    'exercises': [

        # CHEST
        {
            'name': 'Bench Press',
            'description': 'Barbell flat bench press',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': ['Barbell', 'Bench'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Incline Dumbbell Press',
            'description': 'Incline dumbbell chest press',
            'type': 'compound',
            'primary_muscle': 'Upper Chest',
            'requires': ['Dumbbells', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Cable Fly',
            'description': 'Standing cable chest fly',
            'type': 'isolation',
            'primary_muscle': 'Chest',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Push-up',
            'description': 'Bodyweight push-up',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': [],
            'goals': ['Build Muscle', 'Lose Fat'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },

        # BACK
        {
            'name': 'Pull-up',
            'description': 'Bodyweight pull-up',
            'type': 'compound',
            'primary_muscle': 'Lats',
            'requires': ['Pull-up Bar'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Lat Pulldown',
            'description': 'Wide-grip lat pulldown',
            'type': 'compound',
            'primary_muscle': 'Lats',
            'requires': ['Lat Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Seated Row',
            'description': 'Cable seated row',
            'type': 'compound',
            'primary_muscle': 'Back',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Barbell Row',
            'description': 'Bent-over barbell row',
            'type': 'compound',
            'primary_muscle': 'Back',
            'requires': ['Barbell'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },

        # SHOULDERS
        {
            'name': 'Overhead Press',
            'description': 'Standing barbell shoulder press',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': ['Barbell'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Dumbbell Shoulder Press',
            'description': 'Seated dumbbell shoulder press',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Lateral Raises',
            'description': 'Dumbbell side raises',
            'type': 'isolation',
            'primary_muscle': 'Side Delts',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Face Pull',
            'description': 'Cable face pulls for rear delts and posture',
            'type': 'isolation',
            'primary_muscle': 'Rear Delts',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle', 'Fix Posture'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },

        # LEGS
        {
            'name': 'Barbell Squat',
            'description': 'Back squat with barbell',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Barbell', 'Rack'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Knee Pain', 'Lower Back Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Leg Press',
            'description': 'Machine leg press',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Leg Press Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Romanian Deadlift',
            'description': 'Hip hinge for hamstrings',
            'type': 'compound',
            'primary_muscle': 'Hamstrings',
            'requires': ['Barbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Calf Raise',
            'description': 'Standing calf raise',
            'type': 'isolation',
            'primary_muscle': 'Calves',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },

        # ARMS
        {
            'name': 'Bicep Curl',
            'description': 'Standing dumbbell curl',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Hammer Curl',
            'description': 'Neutral grip dumbbell curl',
            'type': 'isolation',
            'primary_muscle': 'Brachialis',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Tricep Rope Pushdown',
            'description': 'Cable triceps pushdown',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Dips',
            'description': 'Bodyweight parallel bar dips',
            'type': 'compound',
            'primary_muscle': 'Triceps',
            'requires': ['Dip Bars'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        # ============================
        # CHUNK 2 — LEGS / ARMS / ABS / CONDITIONING
        # ============================

        # LEGS — QUADS / GLUTES / HAMSTRINGS
        {
            'name': 'Walking Lunge',
            'description': 'Forward alternating lunges',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Bulgarian Split Squat',
            'description': 'Rear-foot elevated split squat',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Dumbbells', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Hip Thrust',
            'description': 'Glute-focused hip thrust',
            'type': 'compound',
            'primary_muscle': 'Glutes',
            'requires': ['Barbell', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Leg Curl Machine',
            'description': 'Hamstring curl machine',
            'type': 'isolation',
            'primary_muscle': 'Hamstrings',
            'requires': ['Leg Curl Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Goblet Squat',
            'description': 'Squat holding a dumbbell at chest',
            'type': 'compound',
            'primary_muscle': 'Quads',
            'requires': ['Dumbbell'],
            'goals': ['Build Muscle', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Step-Up',
            'description': 'Step onto bench with dumbbells',
            'type': 'compound',
            'primary_muscle': 'Glutes',
            'requires': ['Bench', 'Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },

        # ARMS — BICEPS / TRICEPS / FOREARMS
        {
            'name': 'EZ Bar Curl',
            'description': 'Curl using EZ curl bar',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['EZ Bar'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Preacher Curl',
            'description': 'Isolation curl on preacher bench',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Preacher Bench', 'EZ Bar'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Skull Crushers',
            'description': 'Lying tricep extension with EZ bar',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['EZ Bar', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Close-Grip Bench Press',
            'description': 'Bench press focusing on triceps',
            'type': 'compound',
            'primary_muscle': 'Triceps',
            'requires': ['Barbell', 'Bench'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Reverse Curl',
            'description': 'Forearm + brachialis focused curl',
            'type': 'isolation',
            'primary_muscle': 'Forearms',
            'requires': ['Barbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },

        # ABS — CORE STRENGTH
        {
            'name': 'Plank',
            'description': 'Core stability plank',
            'type': 'isolation',
            'primary_muscle': 'Abs',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Hanging Leg Raise',
            'description': 'Hanging abs leg raise',
            'type': 'isolation',
            'primary_muscle': 'Lower Abs',
            'requires': ['Pull-up Bar'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Hip Flexor Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Cable Crunch',
            'description': 'Rope crunch on cable machine',
            'type': 'isolation',
            'primary_muscle': 'Abs',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Neck Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Russian Twist',
            'description': 'Rotational oblique exercise',
            'type': 'isolation',
            'primary_muscle': 'Obliques',
            'requires': ['Dumbbell'],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Mountain Climbers',
            'description': 'High-intensity core movement',
            'type': 'conditioning',
            'primary_muscle': 'Abs',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Beginner'
        },

        # CONDITIONING — CARDIO / FULL BODY
        {
            'name': 'Burpees',
            'description': 'Full body conditioning movement',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Knee Pain', 'Wrist Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Kettlebell Swing',
            'description': 'Hip hinge ballistic movement',
            'type': 'conditioning',
            'primary_muscle': 'Hamstrings',
            'requires': ['Kettlebell'],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Rowing Machine',
            'description': 'Cardio rowing workout',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Rowing Machine'],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Air Bike',
            'description': 'Assault bike cardio',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Air Bike'],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        # ============================
        # CHUNK 3 — MACHINE EXERCISES
        # ============================

        {
            'name': 'Chest Press Machine',
            'description': 'Seated machine chest press',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': ['Chest Press Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Pec Deck Fly',
            'description': 'Chest isolation machine fly',
            'type': 'isolation',
            'primary_muscle': 'Chest',
            'requires': ['Pec Deck Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Hammer Strength Row',
            'description': 'Plate-loaded horizontal row',
            'type': 'compound',
            'primary_muscle': 'Back',
            'requires': ['Hammer Strength Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Back Extension',
            'description': 'Lower back extension machine',
            'type': 'isolation',
            'primary_muscle': 'Lower Back',
            'requires': ['Back Extension Machine'],
            'goals': ['Strength', 'Conditioning'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Seated Leg Extension',
            'description': 'Quad-focused isolation machine',
            'type': 'isolation',
            'primary_muscle': 'Quadriceps',
            'requires': ['Leg Extension Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Hack Squat',
            'description': '45-degree machine squat',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Hack Squat Machine'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Knee Pain', 'Lower Back Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Seated Calf Raise Machine',
            'description': 'Calf isolation machine',
            'type': 'isolation',
            'primary_muscle': 'Calves',
            'requires': ['Calf Raise Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Hip Abductor Machine',
            'description': 'Outer glutes isolation',
            'type': 'isolation',
            'primary_muscle': 'Glutes',
            'requires': ['Abductor Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Hip Adductor Machine',
            'description': 'Inner thighs isolation',
            'type': 'isolation',
            'primary_muscle': 'Adductors',
            'requires': ['Adductor Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Leg Press (Horizontal)',
            'description': 'Horizontal sled press',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Horizontal Leg Press Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Lat Pullover Machine',
            'description': 'Machine for lat isolation',
            'type': 'isolation',
            'primary_muscle': 'Lats',
            'requires': ['Pullover Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Cable Triceps Overhead Extension',
            'description': 'Overhead cable triceps extension',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Cable Bicep Curl',
            'description': 'Standing cable curl',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Cable Lateral Raise',
            'description': 'Single-arm cable side raise',
            'type': 'isolation',
            'primary_muscle': 'Side Delts',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Seated Chest Press (Plate Loaded)',
            'description': 'Hammer Strength chest press',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': ['Plate Loaded Machine'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
# ============================
# CHUNK 4 — ATHLETIC / FULL BODY / STABILITY / ADVANCED
# ============================

# FULL BODY / ATHLETIC MOVEMENTS
{
    'name': 'Thruster',
    'description': 'Squat to overhead press using barbell or dumbbells',
    'type': 'compound',
    'primary_muscle': 'Full Body',
    'requires': ['Barbell', 'Dumbbells'],
    'goals': ['Conditioning', 'Lose Fat', 'Build Muscle'],
    'unsafe_for': ['Shoulder Pain', 'Knee Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Clean and Press',
    'description': 'Olympic lift combining clean and overhead press',
    'type': 'compound',
    'primary_muscle': 'Full Body',
    'requires': ['Barbell'],
    'goals': ['Strength', 'Conditioning'],
    'unsafe_for': ['Lower Back Pain', 'Shoulder Pain'],
    'experience': 'Advanced'
},
{
    'name': 'Snatch',
    'description': 'Olympic lift — explosive ground to overhead movement',
    'type': 'compound',
    'primary_muscle': 'Full Body',
    'requires': ['Barbell'],
    'goals': ['Strength', 'Athleticism'],
    'unsafe_for': ['Shoulder Pain', 'Lower Back Pain'],
    'experience': 'Advanced'
},

# CORE + STABILITY
{
    'name': 'Dead Bug',
    'description': 'Core stability anti-extension movement',
    'type': 'isolation',
    'primary_muscle': 'Abs',
    'requires': [],
    'goals': ['Conditioning', 'Fix Posture'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Pallof Press',
    'description': 'Anti-rotation cable core exercise',
    'type': 'isolation',
    'primary_muscle': 'Obliques',
    'requires': ['Cable Machine'],
    'goals': ['Conditioning', 'Fix Posture'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Swiss Ball Rollout',
    'description': 'Ab rollout using stability ball',
    'type': 'isolation',
    'primary_muscle': 'Abs',
    'requires': ['Stability Ball'],
    'goals': ['Build Muscle', 'Conditioning'],
    'unsafe_for': ['Lower Back Pain'],
    'experience': 'Intermediate'
},

# ADVANCED BODYWEIGHT
{
    'name': 'Pistol Squat',
    'description': 'Single-leg squat',
    'type': 'compound',
    'primary_muscle': 'Legs',
    'requires': [],
    'goals': ['Build Muscle', 'Athleticism'],
    'unsafe_for': ['Knee Pain'],
    'experience': 'Advanced'
},
{
    'name': 'Handstand Push-up',
    'description': 'Vertical push-up against wall or free-standing',
    'type': 'compound',
    'primary_muscle': 'Shoulders',
    'requires': [],
    'goals': ['Build Muscle', 'Athleticism'],
    'unsafe_for': ['Neck Pain', 'Shoulder Pain'],
    'experience': 'Advanced'
},
{
    'name': 'Muscle-up',
    'description': 'Pull-up + dip transition on bar or rings',
    'type': 'compound',
    'primary_muscle': 'Back',
    'requires': ['Pull-up Bar'],
    'goals': ['Athleticism', 'Build Muscle'],
    'unsafe_for': ['Shoulder Pain', 'Elbow Pain'],
    'experience': 'Advanced'
},

# FULL BODY — CROSS TRAINING
{
    'name': 'Battle Ropes',
    'description': 'High-intensity rope conditioning',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': ['Battle Ropes'],
    'goals': ['Conditioning', 'Lose Fat'],
    'unsafe_for': ['Shoulder Pain'],
    'experience': 'Beginner'
},
{
    'name': 'Sled Push',
    'description': 'Weighted sled push for power and conditioning',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': ['Sled'],
    'goals': ['Conditioning', 'Build Muscle'],
    'unsafe_for': ['Knee Pain'],
    'experience': 'Beginner'
},
{
    'name': 'Box Jump',
    'description': 'Explosive plyometric jump onto box',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': ['Plyo Box'],
    'goals': ['Athleticism', 'Conditioning'],
    'unsafe_for': ['Knee Pain', 'Ankle Pain'],
    'experience': 'Intermediate'
},

# STABILITY + BALANCE
{
    'name': 'Single-Leg Deadlift',
    'description': 'Balance-focused hinge using dumbbells or bodyweight',
    'type': 'compound',
    'primary_muscle': 'Hamstrings',
    'requires': ['Dumbbells'],
    'goals': ['Build Muscle', 'Fix Posture'],
    'unsafe_for': ['Lower Back Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Bosu Ball Squat',
    'description': 'Squat performed on BOSU stability ball',
    'type': 'compound',
    'primary_muscle': 'Legs',
    'requires': ['Bosu Ball'],
    'goals': ['Stability', 'Athleticism'],
    'unsafe_for': ['Knee Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Renegade Row',
    'description': 'Plank with alternating dumbbell rows',
    'type': 'compound',
    'primary_muscle': 'Back',
    'requires': ['Dumbbells'],
    'goals': ['Conditioning', 'Build Muscle'],
    'unsafe_for': ['Wrist Pain', 'Lower Back Pain'],
    'experience': 'Intermediate'
},
        # ============================
        # CHUNK 4 — HOME / NO-EQUIPMENT EXERCISES
        # ============================

        {
            'name': 'Bodyweight Squat',
            'description': 'Basic air squat with no equipment',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning', 'Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Wall Sit',
            'description': 'Static leg hold against a wall',
            'type': 'isolation',
            'primary_muscle': 'Quadriceps',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Glute Bridge',
            'description': 'Hip lift focusing on glute activation',
            'type': 'isolation',
            'primary_muscle': 'Glutes',
            'requires': [],
            'goals': ['Build Muscle', 'Conditioning'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Single-Leg Glute Bridge',
            'description': 'Unilateral glute activation',
            'type': 'isolation',
            'primary_muscle': 'Glutes',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Reverse Lunge',
            'description': 'Alternating step-back lunge',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Jump Squat',
            'description': 'Explosive plyometric squat',
            'type': 'conditioning',
            'primary_muscle': 'Quadriceps',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Knee Pain', 'Ankle Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'High Knees',
            'description': 'Running in place with high knee lift',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Shin Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Jumping Jacks',
            'description': 'Full-body jumping movement',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Ankle Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Plank Shoulder Taps',
            'description': 'Alternating shoulder taps from plank position',
            'type': 'conditioning',
            'primary_muscle': 'Abs',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Pike Push-up',
            'description': 'Shoulder-focused push-up variation',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Decline Push-up',
            'description': 'Feet elevated push-up',
            'type': 'compound',
            'primary_muscle': 'Upper Chest',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Diamond Push-up',
            'description': 'Close-hand push-up for triceps',
            'type': 'compound',
            'primary_muscle': 'Triceps',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Wide Push-up',
            'description': 'Chest-dominant push-up variation',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Superman Hold',
            'description': 'Lower back & glute extension hold',
            'type': 'isolation',
            'primary_muscle': 'Lower Back',
            'requires': [],
            'goals': ['Build Muscle', 'Fix Posture'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Bird-Dog',
            'description': 'Opposite arm and leg extension',
            'type': 'isolation',
            'primary_muscle': 'Core',
            'requires': [],
            'goals': ['Conditioning', 'Fix Posture'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Dead Bug',
            'description': 'Core anti-rotation exercise',
            'type': 'isolation',
            'primary_muscle': 'Abs',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Side Plank',
            'description': 'Static hold for obliques',
            'type': 'isolation',
            'primary_muscle': 'Obliques',
            'requires': [],
            'goals': ['Conditioning'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Reverse Crunch',
            'description': 'Lower-ab curling movement',
            'type': 'isolation',
            'primary_muscle': 'Lower Abs',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Hip Hinge',
            'description': 'Bodyweight hinge pattern practice',
            'type': 'compound',
            'primary_muscle': 'Hamstrings',
            'requires': [],
            'goals': ['Build Muscle', 'Conditioning'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Toe Touches',
            'description': 'Abs crunch reaching toward toes',
            'type': 'isolation',
            'primary_muscle': 'Abs',
            'requires': [],
            'goals': ['Lose Fat'],
            'unsafe_for': ['Neck Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Inchworm Walkout',
            'description': 'Walk hands out to plank and back',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Bear Crawl',
            'description': 'Quadruped crawl for conditioning',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Split Jump',
            'description': 'Explosive lunge jump',
            'type': 'conditioning',
            'primary_muscle': 'Quads',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Advanced'
        },
        {
            'name': 'Hand Release Push-up',
            'description': 'Chest-to-floor strict push-up',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': [],
            'goals': ['Build Muscle', 'Conditioning'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Isometric Push-up Hold',
            'description': 'Push-up hold at midpoint',
            'type': 'isolation',
            'primary_muscle': 'Chest',
            'requires': [],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        # ============================
        # CHUNK 5 — CARDIO & HIIT / CONDITIONING
        # ============================

        {
            'name': 'Treadmill Jog',
            'description': 'Light jog at steady pace',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Treadmill'],
            'goals': ['Lose Fat', 'Improve Endurance'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Treadmill Sprint',
            'description': 'High-intensity sprint intervals',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Treadmill'],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Knee Pain', 'Ankle Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Incline Walk',
            'description': 'Walking on high incline for fat burn',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Treadmill'],
            'goals': ['Lose Fat', 'Improve Endurance'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Stairmaster Climb',
            'description': 'Climbing stairs machine workout',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Stairmaster'],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Elliptical Ride',
            'description': 'Low-impact cardio session',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Elliptical'],
            'goals': ['Lose Fat', 'Improve Endurance'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Stationary Bike',
            'description': 'Cycling on a stationary bike',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Bike'],
            'goals': ['Lose Fat', 'Improve Endurance'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Bike Sprints',
            'description': 'High-intensity bike intervals',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Bike'],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Rowing Intervals',
            'description': 'High intensity intervals on rower',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Rowing Machine'],
            'goals': ['Lose Fat', 'Improve Endurance'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Shadow Boxing',
            'description': 'Boxing movements without equipment',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Boxer Shuffle',
            'description': 'Light bouncing footwork for conditioning',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Shin Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Battle Ropes Slams',
            'description': 'Explosive rope slams for full body',
            'type': 'conditioning',
            'primary_muscle': 'Shoulders',
            'requires': ['Battle Ropes'],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Sled Push',
            'description': 'Weighted sled push for power/conditioning',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Sled'],
            'goals': ['Conditioning', 'Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Advanced'
        },
        {
            'name': 'Medicine Ball Slams',
            'description': 'Overhead ball slam for explosive power',
            'type': 'conditioning',
            'primary_muscle': 'Core',
            'requires': ['Medicine Ball'],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Jump Rope',
            'description': 'Skipping rope for cardio',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Jump Rope'],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Shin Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Burpee Broad Jump',
            'description': 'Burpee followed by long jump',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Sprint Shuttle Runs',
            'description': 'Short distance sprint bursts',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Hamstring Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Mountain Climbers Sprint',
            'description': 'Fast-paced mountain climber variation',
            'type': 'conditioning',
            'primary_muscle': 'Core',
            'requires': [],
            'goals': ['Lose Fat', 'Conditioning'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Skater Jumps',
            'description': 'Side-to-side athletic jump',
            'type': 'conditioning',
            'primary_muscle': 'Glutes',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Bear Crawl Sprint',
            'description': 'Fast paced bear crawl',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Conditioning'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Sprawls',
            'description': 'Burpee variation used in MMA conditioning',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': [],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Wrist Pain', 'Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Agility Ladder Steps',
            'description': 'Fast footwork using agility ladder',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Agility Ladder'],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        # ============================
        # CHUNK 6 — MACHINE EXERCISES (PART 2)
        # ============================

        {
            'name': 'Pec Deck Fly',
            'description': 'Chest fly machine',
            'type': 'isolation',
            'primary_muscle': 'Chest',
            'requires': ['Pec Deck Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Chest Press',
            'description': 'Seated chest press machine',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': ['Chest Press Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Shoulder Press',
            'description': 'Seated shoulder press machine',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': ['Shoulder Press Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Lateral Raise',
            'description': 'Side delt machine raises',
            'type': 'isolation',
            'primary_muscle': 'Side Delts',
            'requires': ['Lateral Raise Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Rear Delt Fly',
            'description': 'Reverse fly machine',
            'type': 'isolation',
            'primary_muscle': 'Rear Delts',
            'requires': ['Reverse Fly Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Bicep Curl',
            'description': 'Seated biceps curl machine',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Bicep Curl Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Tricep Extension',
            'description': 'Seated triceps extension machine',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['Tricep Extension Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Leg Extension',
            'description': 'Quad-focused leg extension machine',
            'type': 'isolation',
            'primary_muscle': 'Quadriceps',
            'requires': ['Leg Extension Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Hack Squat Machine',
            'description': 'Machine-assisted squat variation',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Hack Squat Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Machine Hip Abduction',
            'description': 'Outer thigh abduction training',
            'type': 'isolation',
            'primary_muscle': 'Glutes',
            'requires': ['Hip Abduction Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Hip Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Hip Adduction',
            'description': 'Inner thigh adduction training',
            'type': 'isolation',
            'primary_muscle': 'Adductors',
            'requires': ['Hip Adduction Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Hip Pain'],
            'experience': 'Beginner'
        },
        {
            'name': '45 Degree Back Extension Machine',
            'description': 'Machine-assisted back extension',
            'type': 'isolation',
            'primary_muscle': 'Lower Back',
            'requires': ['Back Extension Machine'],
            'goals': ['Build Muscle', 'Fix Posture'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Glute Kickback',
            'description': 'Glute-focused kickback machine',
            'type': 'isolation',
            'primary_muscle': 'Glutes',
            'requires': ['Glute Kickback Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Standing Calf Machine',
            'description': 'Standing calf raise machine',
            'type': 'isolation',
            'primary_muscle': 'Calves',
            'requires': ['Standing Calf Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Ankle Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Seated Calf Machine',
            'description': 'Seated calf raise for soleus',
            'type': 'isolation',
            'primary_muscle': 'Calves',
            'requires': ['Seated Calf Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Ankle Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Smith Machine Bench Press',
            'description': 'Bench press using smith machine',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': ['Smith Machine', 'Bench'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Smith Machine Squat',
            'description': 'Squat using smith machine',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Smith Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Cable Lateral Raise',
            'description': 'Cable side raise for delts',
            'type': 'isolation',
            'primary_muscle': 'Side Delts',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Intermediate'
        },
        {
            'name': 'Cable Rear Delt Row',
            'description': 'Face-high row for rear delts',
            'type': 'isolation',
            'primary_muscle': 'Rear Delts',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Intermediate'
        },
        {
            'name': 'Cable Upright Row',
            'description': 'Cable variation of upright row',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Assisted Dip Machine',
            'description': 'Assisted parallel bar dips',
            'type': 'compound',
            'primary_muscle': 'Triceps',
            'requires': ['Assisted Dip Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Assisted Pull-up Machine',
            'description': 'Assisted pull-up training',
            'type': 'compound',
            'primary_muscle': 'Lats',
            'requires': ['Assisted Pull-up Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        # ============================
        # CHUNK 7 — DUMBBELL + BARBELL ONLY
        # ============================

        # DUMBBELL — CHEST
        {
            'name': 'Dumbbell Bench Press',
            'description': 'Flat dumbbell press',
            'type': 'compound',
            'primary_muscle': 'Chest',
            'requires': ['Dumbbells', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Dumbbell Fly',
            'description': 'Flat dumbbell chest fly',
            'type': 'isolation',
            'primary_muscle': 'Chest',
            'requires': ['Dumbbells', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },

        # DUMBBELL — SHOULDERS
        {
            'name': 'Dumbbell Front Raise',
            'description': 'Front delt raise',
            'type': 'isolation',
            'primary_muscle': 'Front Delts',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Dumbbell Arnold Press',
            'description': 'Rotational shoulder press',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },

        # DUMBBELL — BACK
        {
            'name': 'Single Arm Dumbbell Row',
            'description': 'One-arm row on bench',
            'type': 'compound',
            'primary_muscle': 'Back',
            'requires': ['Dumbbell', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Dumbbell Deadlift',
            'description': 'Hip hinge with dumbbells',
            'type': 'compound',
            'primary_muscle': 'Hamstrings',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle', 'Lose Fat'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },

        # DUMBBELL — LEGS
        {
            'name': 'Dumbbell Romanian Deadlift',
            'description': 'Hamstring hinge with dumbbells',
            'type': 'compound',
            'primary_muscle': 'Hamstrings',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Dumbbell Stepback Lunge',
            'description': 'Reverse lunge with dumbbells',
            'type': 'compound',
            'primary_muscle': 'Glutes',
            'requires': ['Dumbbells'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Dumbbell Sumo Squat',
            'description': 'Sumo stance squat holding dumbbell',
            'type': 'compound',
            'primary_muscle': 'Glutes',
            'requires': ['Dumbbell'],
            'goals': ['Build Muscle', 'Lose Fat'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },

        # DUMBBELL — ARMS
        {
            'name': 'Dumbbell Concentration Curl',
            'description': 'Seated isolation curl',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Dumbbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Dumbbell Overhead Tricep Extension',
            'description': 'Single dumbbell overhead extension',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['Dumbbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Beginner'
        },

        # BARBELL — CHEST
        {
            'name': 'Barbell Close Grip Bench',
            'description': 'Close grip bench for triceps & chest',
            'type': 'compound',
            'primary_muscle': 'Triceps',
            'requires': ['Barbell', 'Bench'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Wrist Pain', 'Shoulder Pain'],
            'experience': 'Intermediate'
        },

        # BARBELL — BACK
        {
            'name': 'Barbell T-Bar Row',
            'description': 'Barbell landmine row variation',
            'type': 'compound',
            'primary_muscle': 'Back',
            'requires': ['Barbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },

        # BARBELL — SHOULDERS
        {
            'name': 'Barbell Upright Row',
            'description': 'Vertical pull for shoulders & traps',
            'type': 'compound',
            'primary_muscle': 'Traps',
            'requires': ['Barbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Intermediate'
        },

        # BARBELL — LEGS
        {
            'name': 'Front Squat',
            'description': 'Quad-dominant front squat',
            'type': 'compound',
            'primary_muscle': 'Quadriceps',
            'requires': ['Barbell', 'Rack'],
            'goals': ['Build Muscle', 'Strength'],
            'unsafe_for': ['Wrist Pain', 'Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Barbell Hip Thrust',
            'description': 'Barbell glute hip thrust',
            'type': 'compound',
            'primary_muscle': 'Glutes',
            'requires': ['Barbell', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },

        # BARBELL — ARMS
        {
            'name': 'Barbell Curl',
            'description': 'Classic barbell biceps curl',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Barbell'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Wrist Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Barbell Skull Crusher',
            'description': 'Lying tricep extension with straight bar',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['Barbell', 'Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Intermediate'
        },
        # ============================
        # CHUNK 8 — ADVANCED / ATHLETIC / ACCESSORY MOVEMENTS
        # (FINAL CHUNK)
        # ============================

        # ATHLETIC / POWER
        {
            'name': 'Box Jump',
            'description': 'Explosive jump onto a plyo box',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Plyo Box'],
            'goals': ['Conditioning', 'Lose Fat', 'Athleticism'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Power Clean',
            'description': 'Olympic lifting movement for power',
            'type': 'compound',
            'primary_muscle': 'Full Body',
            'requires': ['Barbell'],
            'goals': ['Strength', 'Athleticism'],
            'unsafe_for': ['Lower Back Pain', 'Wrist Pain', 'Shoulder Pain'],
            'experience': 'Advanced'
        },

        # GLUTES / HAMSTRINGS
        {
            'name': 'Glute Kickback Machine',
            'description': 'Machine-based glute kickback',
            'type': 'isolation',
            'primary_muscle': 'Glutes',
            'requires': ['Kickback Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Nordic Hamstring Curl',
            'description': 'Bodyweight hamstring eccentric movement',
            'type': 'isolation',
            'primary_muscle': 'Hamstrings',
            'requires': [],
            'goals': ['Build Muscle', 'Athleticism'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Advanced'
        },

        # CALVES
        {
            'name': 'Seated Calf Raise',
            'description': 'Machine seated calf raise',
            'type': 'isolation',
            'primary_muscle': 'Calves',
            'requires': ['Seated Calf Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },

        # SHOULDERS — ADVANCED
        {
            'name': 'Machine Shoulder Press',
            'description': 'Guided shoulder press machine',
            'type': 'compound',
            'primary_muscle': 'Shoulders',
            'requires': ['Shoulder Press Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Lateral Raise',
            'description': 'Isolation machine lateral raise',
            'type': 'isolation',
            'primary_muscle': 'Side Delts',
            'requires': ['Lateral Raise Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },

        # BACK — ADVANCED
        {
            'name': 'Chest Supported Row',
            'description': 'Row with chest support to reduce back strain',
            'type': 'compound',
            'primary_muscle': 'Back',
            'requires': ['Chest Supported Row Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },
        {
            'name': 'Machine Lower Back Extension',
            'description': 'Extension for spinal erectors',
            'type': 'isolation',
            'primary_muscle': 'Lower Back',
            'requires': ['Back Extension Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Beginner'
        },

        # CHEST — ACCESSORY
        {
            'name': 'Pec Deck Machine',
            'description': 'Machine chest fly',
            'type': 'isolation',
            'primary_muscle': 'Chest',
            'requires': ['Pec Deck Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Shoulder Pain'],
            'experience': 'Beginner'
        },

        # ARMS — ADVANCED
        {
            'name': 'Cable Overhead Tricep Extension',
            'description': 'Overhead cable movement for long head of triceps',
            'type': 'isolation',
            'primary_muscle': 'Triceps',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Elbow Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Cable Hammer Curl',
            'description': 'Rope curl with neutral grip',
            'type': 'isolation',
            'primary_muscle': 'Biceps',
            'requires': ['Cable Machine'],
            'goals': ['Build Muscle'],
            'unsafe_for': [],
            'experience': 'Beginner'
        },

        # ABS — ADVANCED
        {
            'name': 'Ab Wheel Rollout',
            'description': 'Advanced core anti-extension exercise',
            'type': 'isolation',
            'primary_muscle': 'Abs',
            'requires': ['Ab Wheel'],
            'goals': ['Build Muscle', 'Athleticism'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },
        {
            'name': 'Weighted Decline Sit-Up',
            'description': 'Inclined sit-up with weight plate',
            'type': 'isolation',
            'primary_muscle': 'Abs',
            'requires': ['Decline Bench'],
            'goals': ['Build Muscle'],
            'unsafe_for': ['Lower Back Pain'],
            'experience': 'Intermediate'
        },

        # CONDITIONING — FINAL ADDITIONS
        {
            'name': 'Sled Push',
            'description': 'Pushing weighted sled for conditioning & legs',
            'type': 'conditioning',
            'primary_muscle': 'Legs',
            'requires': ['Sled'],
            'goals': ['Lose Fat', 'Conditioning', 'Athleticism'],
            'unsafe_for': ['Knee Pain'],
            'experience': 'Beginner'
        },
        {
            'name': 'Battle Ropes',
            'description': 'High-intensity rope slams',
            'type': 'conditioning',
            'primary_muscle': 'Full Body',
            'requires': ['Battle Ropes'],
            'goals': ['Conditioning', 'Lose Fat'],
            'unsafe_for': ['Wrist Pain', 'Shoulder Pain'],
            'experience': 'Beginner'
        },
# ============================
# CHUNK 9 — ENDURANCE / LOW-IMPACT / INJURY-SAFE
# ============================

{
    'name': 'Incline Walk',
    'description': 'Treadmill incline fast walking',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': ['Treadmill'],
    'goals': ['Improve Endurance', 'Lose Fat'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Light Cycling',
    'description': 'Stationary bike low-impact cardio',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': ['Stationary Bike'],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Elliptical Trainer',
    'description': 'Low-impact elliptical cardio',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': ['Elliptical'],
    'goals': ['Improve Endurance', 'Lose Fat'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Rowing Machine Steady Pace',
    'description': 'Moderate-intensity rowing session',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': ['Rowing Machine'],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Air Bike Intervals (Light)',
    'description': 'Low-strain endurance intervals on air bike',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': ['Air Bike'],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Walking',
    'description': 'Outdoor or treadmill walking',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': [],
    'goals': ['Improve Endurance', 'Lose Fat'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Marching in Place',
    'description': 'Low-impact marching movement',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Step Jacks',
    'description': 'Low-impact alternative to jumping jacks',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Shadow Boxing (Low-Impact)',
    'description': 'Slow tempo shadow boxing for endurance',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': ['Shoulder Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Walking Lunges (Short Range)',
    'description': 'Low-depth lunges for endurance and balance',
    'type': 'conditioning',
    'primary_muscle': 'Glutes',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': ['Knee Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Glute Bridge March',
    'description': 'Alternating leg bridge march',
    'type': 'conditioning',
    'primary_muscle': 'Glutes',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Bird Dog Reach',
    'description': 'Core stability movement with long holds',
    'type': 'conditioning',
    'primary_muscle': 'Core',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Dead Bug',
    'description': 'Slow, controlled core movement',
    'type': 'conditioning',
    'primary_muscle': 'Abs',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Side Step Walk',
    'description': 'Lateral movement endurance drill',
    'type': 'conditioning',
    'primary_muscle': 'Glutes',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Treadmill Light Jog',
    'description': 'Slow jogging pace for endurance',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': ['Treadmill'],
    'goals': ['Improve Endurance'],
    'unsafe_for': ['Knee Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Farmers Carry (Light)',
    'description': 'Walking with light dumbbells',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': ['Dumbbells'],
    'goals': ['Improve Endurance'],
    'unsafe_for': ['Lower Back Pain'],
    'experience': 'Beginner'
},
{
    'name': 'Boxing Footwork Drill',
    'description': 'Step patterns for endurance',
    'type': 'conditioning',
    'primary_muscle': 'Legs',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': ['Knee Pain'],
    'experience': 'Intermediate'
},
{
    'name': 'Resistance Band Walk',
    'description': 'Lateral and forward band walks',
    'type': 'conditioning',
    'primary_muscle': 'Glutes',
    'requires': ['Resistance Band'],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Stationary Step Touches',
    'description': 'Alternating side step taps',
    'type': 'conditioning',
    'primary_muscle': 'Full Body',
    'requires': [],
    'goals': ['Improve Endurance'],
    'unsafe_for': [],
    'experience': 'Beginner'
},
{
    'name': 'Light Kettlebell Deadlift',
    'description': 'Endurance-focused kettlebell hinge',
    'type': 'conditioning',
    'primary_muscle': 'Glutes',
    'requires': ['Kettlebell'],
    'goals': ['Improve Endurance'],
    'unsafe_for': ['Lower Back Pain'],
    'experience': 'Beginner'
}


    ]
}


# ===========================
# SEED FUNCTION
# ===========================
def seed():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as s:

        # Create uniqueness constraints
        s.run('CREATE CONSTRAINT IF NOT EXISTS FOR (g:Goal) REQUIRE g.name IS UNIQUE')
        s.run('CREATE CONSTRAINT IF NOT EXISTS FOR (e:Exercise) REQUIRE e.name IS UNIQUE')
        s.run('CREATE CONSTRAINT IF NOT EXISTS FOR (eq:Equipment) REQUIRE eq.name IS UNIQUE')
        s.run('CREATE CONSTRAINT IF NOT EXISTS FOR (inj:Injury) REQUIRE inj.name IS UNIQUE')
        s.run('CREATE CONSTRAINT IF NOT EXISTS FOR (lvl:ExperienceLevel) REQUIRE lvl.name IS UNIQUE')

        # Insert exercises
        for ex in seed_data['exercises']:

            # Create exercise node
            s.run(
                '''
                MERGE (e:Exercise {name:$name})
                SET e.description=$description,
                    e.type=$type,
                    e.primary_muscle=$primary_muscle
                ''',
                ex
            )

            # Link goals
            for g in ex['goals']:
                s.run(
                    '''
                    MERGE (go:Goal {name:$goal})
                    MERGE (e:Exercise {name:$name})
                    MERGE (e)-[:FOR_GOAL]->(go)
                    ''',
                    {'goal': g, 'name': ex['name']}
                )

            # Link equipment
            for eq in ex['requires']:
                s.run(
                    '''
                    MERGE (eq:Equipment {name:$eq})
                    MERGE (e:Exercise {name:$name})
                    MERGE (e)-[:REQUIRES]->(eq)
                    ''',
                    {'eq': eq, 'name': ex['name']}
                )

            # Link injuries
            for inj in ex.get('unsafe_for', []):
                s.run(
                    '''
                    MERGE (i:Injury {name:$inj})
                    MERGE (e:Exercise {name:$name})
                    MERGE (e)-[:UNSAFE_FOR]->(i)
                    ''',
                    {'inj': inj, 'name': ex['name']}
                )

            # Link experience
            s.run(
                '''
                MERGE (lvl:ExperienceLevel {name:$lvl})
                MERGE (e:Exercise {name:$name})
                MERGE (e)-[:EXPERIENCE_REQUIRED]->(lvl)
                ''',
                {'lvl': ex['experience'], 'name': ex['name']}
            )

    driver.close()


if __name__ == '__main__':
    seed()
    print("Seeding complete")
