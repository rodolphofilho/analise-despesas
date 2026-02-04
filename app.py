import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px # IMPORTA GRAFICOS


engine = create_engine(
    "mysql+pymysql://root:minhasenha123@localhost/analise_despesas"
)

df = pd.read_sql('SELECT * FROM despesas', engine)


# configuração da pagina

st.set_page_config(
    page_title=
    'DASHBOARD DE DESPESAS', 
    layout='wide')

#TITULOS
st.title('📊 RELATÓRIO DE DESPESAS – CONDOMÍNIO PRESIDENTE')
st.subheader('ANÁLISE MENSAL E ANUAL DE COMPRAS, CONTAS E SALÁRIOS')

#FILTRO LATERAL DO ANO

month = st.sidebar.selectbox(
    'SELECIONE O ANO',
    sorted(df[df['Ano'] != 2022]['Ano'].unique()) # estou excluindo o ano de 2022
)