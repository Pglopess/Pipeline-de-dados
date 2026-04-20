# Pipeline de Dados IMDb — Pandas + SQLite

Pipeline completo de dados utilizando um dataset público de filmes do IMDb. O fluxo inclui ingestão, limpeza, armazenamento em banco SQLite e análise via SQL com geração de relatórios em CSV.

## Dataset

Movies Dataset, disponível no Kaggle:
https://www.kaggle.com/datasets/danielgrijalvas/movies

Contém informações de mais de 7.000 filmes: título, ano, gênero, diretor, bilheteria, nota e número de votos.

## Tecnologias utilizadas

- Python 3.9+
- Pandas
- SQLite (sqlite3)

## Como rodar

1. Clone o repositório
2. Crie e ative o ambiente virtual:
```bash
   py -m venv .venv
   .venv\Scripts\activate
```
3. Instale as dependências:
```bash
   pip install -r requirements.txt
```
4. Baixe o dataset no link acima e salve em `data/movies.csv`
5. Execute os scripts na ordem:
```bash
   py src/ingestion.py
   py src/database.py
   py src/analysis.py
```

## Estrutura do projeto
```
├── src/
│   ├── ingestion.py   # leitura e limpeza dos dados com Pandas
│   ├── database.py    # criacao do banco SQLite e insercao dos dados
│   └── analysis.py    # queries SQL e exportacao dos relatorios
├── data/              # dataset bruto (não versionado)
├── outputs/           # relatórios gerados em CSV
├── requirements.txt
└── README.md
```

## Resultados gerados

- `top10_bilheteria.csv` — os 10 filmes com maior bilheteria
- `media_nota_genero.csv` — média de avaliação por gênero
- `top5_diretores_bilheteria.csv` — os 5 diretores com maior bilheteria total
- `filmes_por_decada.csv` — quantidade de filmes produzidos por década
