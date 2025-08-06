import pandas as pd

# Apontar para o caminho correto
filepath = "steam.csv"
df = pd.read_csv(filepath)
print(df.head())
print(df.columns)
print(df.iloc[0])

# Verificando distribuição de dados
print(df['All Reviews Summary'].head(20))
print(df['All Reviews Summary'].unique())
print(df['All Reviews Summary'].value_counts())
print(pd.isna(df['All Reviews Summary']).sum())
print(pd.isna(df['Recent Reviews Summary']).sum())

# Filtrar por jogos com nota "Overwhelmingly Negative"
result = df['All Reviews Summary'] == "Overwhelmingly Negative"
print(df[result])

# Remover linhas com valores faltantes
subset_df = df[['Release Date','All Reviews Summary']]
print(subset_df.head())
result = subset_df['All Reviews Summary'].isna()
subset_df = subset_df[~result]
result = subset_df['Release Date'].isna()
subset_df = subset_df[~result]
print(subset_df.head(20))

# Extrair o ano da data
print(subset_df['Release Date'].value_counts())
def parse_year(date_str: str) -> int:    
    try:
        print(date_str)
        values = date_str.split(",")
        return int(values[1])
        # date = date_str[-4:]
        # return int(date)
    except:
        return pd.NA # null

year = parse_year("17 Jul, 2023")
print(year + 1)

# Obter os anos de todas as datas
subset_df["year"] = subset_df['Release Date'].map(parse_year)

# Veriicar a distribuição das notas pelos anos
def concat(x: pd.Series) -> str:
    return str(x["year"]) + " " + x["All Reviews Summary"]
subset_df["concat"] = subset_df.apply(concat, axis=1)
print(subset_df["concat"].value_counts())

