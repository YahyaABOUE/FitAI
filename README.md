FitAI – AI Fitness Coach

DESCRIPTION
FitAI est une application d’assistant sportif intelligent qui génère des plans
d’entraînement personnalisés en fonction du profil utilisateur (âge, objectifs,
niveau sportif et contraintes physiques).

Le projet combine une API backend en Python, des techniques d’intelligence
artificielle (embeddings), et une base de données graphe Neo4j afin de produire
des recommandations adaptées et cohérentes.

-----------------------------------------------------------------------

FONCTIONNALITÉS PRINCIPALES
- Création de profils utilisateurs
- Génération automatique de plans d’entraînement
- Adaptation des exercices selon le niveau et les objectifs
- Séparation claire entre backend et frontend

-----------------------------------------------------------------------

TECHNOLOGIES UTILISÉES

Backend :
- Python 3
- FastAPI
- Neo4j (base de données graphe)
- OpenAI API (embeddings et raisonnement)
- Uvicorn

Frontend :
- HTML
- CSS
- JavaScript

-----------------------------------------------------------------------

ARCHITECTURE DU PROJET

FitAI
│
├── backend
│   └── app
│       ├── main.py
│       ├── models.py
│       ├── embeddings_service.py
│       ├── neo4j_client.py
│       ├── prompt_template.py
│       ├── seed_db.py
│       └── requirements.txt
│
├── frontend
│   └── index.html
│
└── README.txt

-----------------------------------------------------------------------

INSTALLATION ET EXÉCUTION

1) Cloner le projet
git clone https://github.com/YahyaABOUE/FitAI.git
cd FitAI

-----------------------------------------------------------------------

2) Créer un environnement virtuel
python -m venv venv

Activation :
Windows :
venv\Scripts\activate

Linux / macOS :
source venv/bin/activate

-----------------------------------------------------------------------

3) Installer les dépendances
pip install -r backend/app/requirements.txt

-----------------------------------------------------------------------

4) Configuration des variables d’environnement

Créer un fichier .env dans le dossier backend/app avec le contenu suivant :

OPENAI_API_KEY=your_openai_key
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

-----------------------------------------------------------------------

5) Lancer le backend
cd backend/app
uvicorn main:app --reload

L’API sera accessible à l’adresse :
http://127.0.0.1:8000

-----------------------------------------------------------------------

6) Lancer le frontend
Ouvrir le fichier frontend/index.html dans un navigateur web.

-----------------------------------------------------------------------

OBJECTIF ACADÉMIQUE
Ce projet a été réalisé dans un cadre académique afin de démontrer :
- L’utilisation d’une API backend moderne (FastAPI)
- L’intégration de l’intelligence artificielle dans une application concrète
- L’exploitation d’une base de données graphe (Neo4j)
- Une architecture logicielle claire et modulaire

-----------------------------------------------------------------------

AUTEURS
- Yahya ABOU EL AZIZ
- Mehdi GUELLIDA
- Younes EL MAJDOUBI EL IDRISSI

-----------------------------------------------------------------------

LICENCE
Projet réalisé à des fins éducatives.
