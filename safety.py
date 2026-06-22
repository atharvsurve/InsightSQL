import re


FORBIDDEN = [

    "INSERT",

    "UPDATE",

    "DELETE",

    "DROP",

    "ALTER",

    "TRUNCATE",

    "CREATE",

    "GRANT",

    "REVOKE"

]


def validate_sql(sql: str):

    sql_upper = sql.upper()


    for word in FORBIDDEN:

        if re.search(r"\b" + word + r"\b", sql_upper):

            raise Exception(

                f"Forbidden SQL detected: {word}"

            )


    if not (

        sql_upper.strip().startswith("SELECT")

        or

        sql_upper.strip().startswith("WITH")

    ):

        raise Exception(

            "Only SELECT queries are allowed"

        )


    return True