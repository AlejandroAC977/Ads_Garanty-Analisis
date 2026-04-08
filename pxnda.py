from df_ads import df

def imprimir():
    print("""
        1: primeras filas
        2: ultimas filas
        3: shape
        4: columnas
        5: dataTypes
        6: info
        7: nulos
        8: duplicados
        9: descripcion
    """)

    seleccion=input("Show: ")

    match seleccion:
        case "1":
            print(df.head())
        case "2":
            print(df.tail())
        case "3":
            print(df.describe())
        case "4":
            print(df.columns)
        case "5":
            print(df.dtypes)
        case "6":
            print(df.info())
        case "7":
            print(df.isnull().sum())
        case "8":
            print(df.duplicated().sum())
        case "9":
            print(df.describe())

imprimir()



