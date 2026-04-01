import pandas as pd

def carregar_dados():
    df = pd.read_csv("data/movies.csv")
    df = df.dropna(subset=["score", "votes", "gross"])
    df = df.fillna({"rating": "Not Rated", "budget": 0})
    df = df.dropna(subset=["runtime"])
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.shape)
    print(df.isnull().sum())