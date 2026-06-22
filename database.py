from sqlalchemy import create_engine, inspect, text
from config import config


class Database:

    def __init__(self):

        self.engine = create_engine(
            config.DATABASE_URL,
            pool_pre_ping=True,
            future=True
        )

        self.inspector = inspect(self.engine)

        self.schema_cache = None


    def test_connection(self):

        with self.engine.connect() as conn:

            return conn.execute(text("SELECT 1")).scalar()


    def get_schema(self):

        if self.schema_cache:
            return self.schema_cache

        schema = ""

        tables = self.inspector.get_table_names()

        for table in tables:

            schema += f"\nTABLE: {table}\n"

            columns = self.inspector.get_columns(table)

            for col in columns:

                schema += f"{col['name']} ({col['type']})\n"

        self.schema_cache = schema

        return schema


    def execute_query(self, sql):

        with self.engine.connect() as conn:

            result = conn.execute(text(sql))

            return [dict(row._mapping) for row in result.fetchall()]


db = Database()