import pandas as pd
import sqlite3

conn = sqlite3.connect("data/movies.db")

# Top 10 filmes com maior bilheteria
df_top = pd.read_sql("SELECT name, gross FROM movies ORDER BY gross DESC LIMIT 10", conn)
df_top.to_csv("outputs/top10_bilheteria.csv", index=False)
print("Top 10 filmes com maior bilheteria:")
for index, row in df_top.iterrows():
    print(f"{row['name']}: ${row['gross']}")

# Média de nota por gênero
df_genero = pd.read_sql("SELECT genre, AVG(score) AS media_score FROM movies GROUP BY genre", conn)
df_genero.to_csv("outputs/media_nota_genero.csv", index=False)
print("\nMédia de nota por gênero:")
for index, row in df_genero.iterrows():
    print(f"{row['genre']}: {row['media_score']:.2f}")

# Os 5 diretores com maior bilheteria total
df_diretores = pd.read_sql("SELECT director, SUM(gross) AS total_gross FROM movies GROUP BY director ORDER BY total_gross DESC LIMIT 5", conn)
df_diretores.to_csv("outputs/top5_diretores_bilheteria.csv", index=False)
print("\nOs 5 diretores com maior bilheteria total:")
for index, row in df_diretores.iterrows():
    print(f"{row['director']}: ${row['total_gross']}")

# Quantidade de filmes por década
df_decada = pd.read_sql("SELECT (year / 10) * 10 AS decade, COUNT(*) AS total FROM movies GROUP BY decade ORDER BY decade", conn)
df_decada.to_csv("outputs/filmes_por_decada.csv", index=False)
print("\nQuantidade de filmes por década:")
for index, row in df_decada.iterrows():
    print(f"{int(row['decade'])}s: {int(row['total'])} filmes")

conn.close()