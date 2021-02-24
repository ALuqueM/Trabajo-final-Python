#importa pandas
import pandas as pd
# Crea una Serie de los numeros 10, 20 and 10.
serie= [10,20,10]
print(serie)
# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
colores= ['rojo','verde','azul']
print(colores)
# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()
# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
df =pd.DataFrame(serie)
print(df)
# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df =pd.DataFrame(serie,colores)
print(df)
# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"

df = pd.read_csv('./data/pandas/avengers.csv')
print(df)
# Muestra las primeras 5 filas del DataFrame.

print(df.head())
# Muestra las primeras 10 filas del DataFrame. 
print(df.head(10))
# Muestra las últimas 5 filas del DataFrame.
print(df.tail())
# Muestra el tamaño del DataFrame
print(df.shape)
# Muestra los data types del dataframe
print(df.dtypes)
# Cambia el indice a la columna "fecha_inicio".

df.loc[5]
df2 = df.set_index("fecha_inicio")
print(df2)
# Ordena el índice de forma descendiente
df_sorted = df2.sort_values(by=["fecha_inicio"], ascending=False)
print(df_sorted)

# Resetea el índice

f2 = df2.reset_index(drop=True)
print(f2)

