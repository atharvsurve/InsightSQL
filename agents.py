from google import genai

from config import config

from prompts import (

    SQL_SYSTEM_PROMPT,

    ANSWER_PROMPT

)

from database import Database


client = genai.Client(

    api_key=config.GEMINI_API_KEY

)

db = Database()


def schema_agent():

    schema = db.get_schema()

    return schema

def sql_agent(

        question,

        schema

):

    prompt = f"""

{SQL_SYSTEM_PROMPT}


Schema:

{schema}


Question:

{question}


Generate SQL only.

"""


    response = client.models.generate_content(

        model=config.MODEL_NAME,

        contents=prompt

    )


    sql = response.text.strip()


    sql = sql.replace(

        "```sql",

        ""

    )


    sql = sql.replace(

        "```",

        ""

    )


    return sql


def database_agent(sql):

    rows = db.execute_query(sql)

    return rows

def answer_agent(

        question,

        result

):

    prompt = ANSWER_PROMPT.format(

        question=question,

        result=result

    )


    response = client.models.generate_content(

        model=config.MODEL_NAME,

        contents=prompt

    )


    return response.text


