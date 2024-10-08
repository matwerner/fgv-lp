import pandas as pd

# Apontar para o caminho correto
filepath = "vgsales.csv"
df = pd.read_csv(filepath, sep=",")
print(df.index)
print(df.columns)
print(df.shape)
print(df.dtypes)

print(df.head())
print(df.columns)

# Filtrar as colunas
# -> Concentrar nos dados a serem analisados
# -> Diminui tamanho do arquivo
columns = ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'Global_Sales']
subset_df = df[columns]
subset_df.to_csv('subset.csv', index=False)

print(subset_df.head())

# Indexar pelo campo Name em vez de 0 a n-1
columns = ["Name", "Genre", "Platform"]
sub_df = df[columns]
sub_df2 = sub_df.set_index("Name")
print(sub_df2)

# Pegar parte das linhas
print(sub_df2.iloc[10:20])
print(sub_df2.loc["Pokemon Red/Pokemon Blue"])
print(df[df["Global_Sales"] >= 1.0])

# Criando nova coluna valores
head_df = df.head().copy()
head_df["type"] = ["Retro", "Retro", "Modern", "Modern", "Modern"]
print(head_df)
# Removendo coluna
head_df.drop("type", axis=1, inplace=True)
print(head_df)

# Inserindo nova linha
sub_df = sub_df.copy()
new_row = {
    "Name": "Mario Demo",
    "Genre": "Plataform",
    "Platform": "Switch 2",
}
new_df = pd.DataFrame([new_row])
print(new_df)
print(pd.concat([df, new_df], ignore_index=True))

# Quantidade de jogos por genero
genre_counter = df["Genre"].value_counts()
print(100 * genre_counter / df.shape[0])

# Tratamento de dados
sale_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

def compute_mean(x: pd.Series):
    return x.mean()

print(df[sale_columns].apply(compute_mean, axis=0))
for column in sale_columns:
    print(compute_mean(df[column]))

print(df[sale_columns].apply(compute_mean, axis=1))
for idx, row in df.iterrows():    
    print(row[sale_columns].mean())
    # Sõ para verificar a primeira linha
    break
