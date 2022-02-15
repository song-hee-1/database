from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import psycopg2.extras


app = FastAPI()

# Update connection string information
host = "<server-name>"
dbname = "<database-name>"
user = "<admin-username>"
password = "<admin-password>"
sslmode = "require"


# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()

class Fruit(BaseModel):
    id: int
    name: str
    season: str
    description: str
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    cursor.execute("Select * FROM public.fruits1 LIMIT 0")
    colnames = [desc[0] for desc in cursor.description]

    cursor.execute("SELECT * FROM public.fruits1;")

    fruit = []
    for row in cursor.fetchall():
        fruit.append(dict(zip(colnames, row)))
    return fruit

@app.get("/fruits/{fruit_id}")
def read_fruit(fruit_id: int):
    cursor.execute("Select * FROM public.fruits1 LIMIT 0")
    colnames = [desc[0] for desc in cursor.description]

    cursor.execute(f"SELECT * FROM public.fruits1 WHERE id={fruit_id}")

    fruit = []
    for row in cursor.fetchall():
        fruit.append(dict(zip(colnames, row)))
    return fruit

