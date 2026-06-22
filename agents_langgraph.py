from database import db

def schema_agent(state):

    return {

        "schema": db.get_schema()

    }
    
    
def planner_agent(state):

    question = state["question"]

    return {

        "question": question
    }

from google import genai
from config import config

client = genai.Client(api_key=config.GEMINI_API_KEY)


def sql_agent(state):

    prompt = f"""

You are an expert PostgreSQL engineer.

RULES:
- Use ONLY schema columns exactly
- Never hallucinate column names
- Use snake_case only
- Return ONLY SQL

Schema:
{state['schema']}

Question:
{state['question']}

"""

    res = client.models.generate_content(

        model=config.MODEL_NAME,

        contents=prompt

    )

    return {

        "sql": res.text.strip().replace("```sql","").replace("```","")

    }
    
from database import db

def execute_agent(state):

    try:

        result = db.execute_query(state["sql"])

        return {

            "result": result,

            "error": None

        }

    except Exception as e:

        return {

            "error": str(e),

            "result": None

        }
        
def fixer_agent(state):

    error = state["error"]

    prompt = f"""

Fix this SQL error:

ERROR:
{error}

SQL:
{state['sql']}

Schema:
{state['schema']}

Return ONLY corrected SQL.
"""

    res = client.models.generate_content(

        model=config.MODEL_NAME,

        contents=prompt

    )

    return {

        "sql": res.text.strip().replace("```sql","").replace("```","")

    }
    
def answer_agent(state):

    prompt = f"""

User Question:
{state['question']}

SQL Result:
{state['result']}

Explain the answer clearly.
"""

    res = client.models.generate_content(

        model=config.MODEL_NAME,

        contents=prompt

    )

    return {

        "final_answer": res.text
    }
    
