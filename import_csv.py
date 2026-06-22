import pandas as pd

from sqlalchemy import create_engine

import os


DATABASE_URL = (

    "postgresql://postgres:Atharv%401604@localhost:5433/SalesApple"

)


engine = create_engine(DATABASE_URL)


folder = "data"


for file in os.listdir(folder):

    if file.endswith(".csv"):


        filepath = os.path.join(folder,file)


        table_name = file.replace(".csv","").lower()


        print(f"Importing {table_name}")


        df = pd.read_csv(filepath)


        print(df.head())


        df.to_sql(

            table_name,

            engine,

            if_exists="replace",

            index=False,

            method="multi"

        )


        print(f"{table_name} imported")


print("Done")

