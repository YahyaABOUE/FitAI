from neo4j import GraphDatabase
import os

class Neo4jClient:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "test1234")

        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_filtered_exercises(self, goal, equipment, injuries, experience):
        query = """
        MATCH (e:Exercise)-[:FOR_GOAL]->(g:Goal {name: $goal})
        MATCH (e)-[:EXPERIENCE_REQUIRED]->(lvl:ExperienceLevel {name: $experience})

        WHERE NOT EXISTS {
            MATCH (e)-[:UNSAFE_FOR]->(inj:Injury)
            WHERE inj.name IN $injuries
        }

        OPTIONAL MATCH (e)-[:REQUIRES]->(eq:Equipment)
        WITH e, COLLECT(eq.name) AS required_equipment

        WHERE (
            SIZE(required_equipment) = 0
            OR ALL(req IN required_equipment WHERE req IN $equipment)
        )

        RETURN e {
            .name,
            .description,
            .type,
            .primary_muscle,
            requires: required_equipment
        } AS exercise
        """

        with self.driver.session() as session:
            res = session.run(
                query,
                {
                    "goal": goal,
                    "equipment": equipment,
                    "injuries": injuries,
                    "experience": experience
                }
            )
            return [record["exercise"] for record in res]

    def close(self):
        self.driver.close()
