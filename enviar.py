import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Banco de dados

load_dotenv()

user = os.getenv('BD_USER')
password = os.getenv('BD_PASSWORD')
host = os.getenv('BD_HOST')
bd = os.getenv('BD_NAME')
arquivo = os.getenv('BD_ARQUIVO')


print('Lendo Excel...')

#importar os dodos do excel
df = pd.read_excel('Dados_Tratados.xlsx')


#valor
df['Valor'] = (
    df['Valor']
    .astype(str)
    .str.replace('R$', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '', regex=False)

)

df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)

#Transformando em data

df["Data_Vencimento"] = pd.to_datetime(df["Data_Vencimento"], errors="coerce").dt.date
df["Data_Pagamento"] = pd.to_datetime(df["Data_Pagamento"], errors="coerce").dt.date

print('Conectando ao Mysql')

#Criar conecxão com mysql
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{bd}"
)

print("Enviando dados")
df.to_sql("despesas", engine, if_exists="replace", index=False)

print("IMPORTAÇÃO FINALIZADA COM SUCESSO!")
