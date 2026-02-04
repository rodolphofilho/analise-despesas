import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:minhasenha123@localhost/analise_despesas"
)

df = pd.read_sql('SELECT * FROM despesas', engine)

print(df.head())