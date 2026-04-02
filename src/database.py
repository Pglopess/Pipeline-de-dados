import pandas as pd
import sqlite3
from ingestion import carregar_dados

df = carregar_dados()

conn = sqlite3.connect("data/movies.db")

cursor = conn.cursor()

df.to_sql("movies", conn, if_exists="replace", index=False)

cursor.execute("SELECT COUNT(*) FROM movies")

print(cursor.fetchone())

conn.close()