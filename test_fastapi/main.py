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
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

class Fruit(BaseModel):
    id: int
    name: str
    season: str
    description: str
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    cursor.execute("SELECT * FROM public.fruits1;")
    rows = cursor.fetchall()
    return rows

    for fruit in rows:
        fruit.append(dict(rows))
        return fruit

@app.get("/fruits/{fruit_id}")
def read_fruit(fruit_id: int, fr, q: Optional[str] = None):
    return {"fruit_id": fruit_id, "q": q}

@app.put("/fruits/{fruit_id}")
def update_fruit(fruit_id: int, fruit: Fruit):
    return {"fruit_id": fruit.id, "fruit_name": fruit.name, "fruit_season": fruit.season, "fruit_description": fruit.description}
