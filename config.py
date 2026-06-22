from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    # Gemini API Key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Model
    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gemini-2.5-flash"
    )

    # Universal Database URL
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Max rows returned from SQL
    MAX_ROWS = int(
        os.getenv(
            "MAX_ROWS",
            "100"
        )
    )

    # SQL timeout in seconds
    SQL_TIMEOUT = int(
        os.getenv(
            "SQL_TIMEOUT",
            "30"
        )
    )


config = Config()