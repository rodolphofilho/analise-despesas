import pandas as pd


# Ler arquivo bruto

df = pd.read_csv("Despesas.csv")

# Padronizar colunas

df.columns = df.columns.str.strip()
df.columns = df.columns.str.upper()

# Renomear colunas

df = df.rename(columns={
    "MES": "Mes",
    "RELAÇÃO DAS DESPESAS REFERENTE O ANO DE": "Descricao",
    "SAÍDAS": "Saida",
    "ENTRADA": "Entrada",
    "ANO": "Ano",
    "DATA VENC": "Data_Vencimento",
    "DATA PAG": "Data_Pagamento",
    "QUANTIDADE": "Quantidade"
})

# Criar coluna Valor

df["Valor"] = df["Saida"].fillna(df["Entrada"])

# Criar coluna Tipo

df["Tipo"] = df["Entrada"].apply(
    lambda x: "Entrada" if pd.notna(x) else "Saida"
)

# Remover linhas sem valor

df = df[df["Valor"].notna()]

# Criar Categoria automática

def classificar(texto):

    texto = str(texto).lower()

    if "energia" in texto:
        return "Energia"
    if "construção" in texto or "construcao" in texto:
        return "Material de Construção"
    if "limpeza" in texto or 'sacos' in texto:
        return "Material de Limpeza"
    if "fundo" in texto or "fgts" in texto:
        return "Fgts"
    if "internet" in texto:
        return "Internet"
    if "agua" in texto or "água" in texto:
        return "Distribuidora de Água"
    if "quizena" in texto or "ferias" in texto or "salario" in texto:
        return "Salario"
    if "receita federal" in texto or "imposto" in texto:
        return "Imposto"
    if 'vale' in texto:
        return 'Benefícios' 
    else:
        return "Outros"

df["Categoria"] = df["Descricao"].apply(classificar)


# Colunas finais

df = df[
    [
        "Mes",
        "Descricao",
        "Categoria",
        "Tipo",
        "Valor",
        "Ano",
        "Data_Vencimento",
        "Data_Pagamento",
        "Quantidade"
    ]
]


# Salvar arquivo tratado


df.to_excel("Dados_Tratados.xlsx", index=False)

print("LIMPEZA FINALIZADA COM SUCESSO!")
print(df.head())
