from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import psycopg2


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

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    cursor.execute("SELECT * FROM public.fruits1;")
    rows = cursor.fetchall()
    # Print all rows

    fruitsArray = []
    for item in rows:
        fruitsArray.append(rows)
        return fruitsArray

