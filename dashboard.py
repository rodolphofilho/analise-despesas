import streamlit as st
import pandas as pd
import plotly.express as px


# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title='Dashboard de Vendas - Supermercado',
    layout='wide'
)

# CARREGAMENTO DOS DADOS
#

@st.cache_data
def load_data():
    df = pd.read_csv('supermarket_sales.csv', sep=',', decimal=',')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df

df = load_data()

# TÍTULOS

st.title('📊 Dashboard de Desempenho de Vendas - Supermercado')
st.subheader('Análise mensal de faturamento, produtos e avaliações')

# FILTRO LATERAL
month = st.sidebar.selectbox(
    'Selecione o mês',
    sorted(df['Month'].unique())
)

df_filtered = df[df['Month'] == month]

# LAYOUT
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# FATURAMENTO POR DIA
fig_date = px.bar(
    df_filtered,
    x='Date',
    y='Total',
    color='CIDADE',
    title='Faturamento por Dia'
)
col1.plotly_chart(fig_date, use_container_width=True)

# FATURAMENTO POR PRODUTO

prod_total = (
    df_filtered
    .groupby(['PRODUTOS', 'CIDADE'])[['Total']]
    .sum()
    .reset_index()
)

fig_prod = px.bar(
    prod_total,
    x='Total',
    y='PRODUTOS',
    color='CIDADE',
    title='Faturamento por Linha de Produto',
    orientation='h'
)
col2.plotly_chart(fig_prod, use_container_width=True)

# FATURAMENTO POR CIDADE
city_total = (
    df_filtered
    .groupby('CIDADE')[['Total']]
    .sum()
    .reset_index()
)

fig_city = px.bar(
    city_total,
    x='CIDADE',
    y='Total',
    title='Faturamento por Cidade'
)
col3.plotly_chart(fig_city, use_container_width=True)

# FATURAMENTO POR PAGAMENTO
fig_payment = px.pie(
    df_filtered,
    values='Total',
    names='PAGAMENTOS',
    title='Faturamento por Tipo de Pagamento'
)
col4.plotly_chart(fig_payment, use_container_width=True)

# AVALIAÇÃO MÉDIA POR CIDADE

rating_city = (
    df_filtered
    .groupby('CIDADE')[['Rating']]
    .mean()
    .reset_index()
)

fig_rating = px.bar(
    rating_city,
    x='CIDADE',
    y='Rating',
    title='Avaliação Média por Cidade',
    
)
col5.plotly_chart(fig_rating, use_container_width=True)
