import pandas as pd

def manipular_texto(texto):
    df = pd.DataFrame({'Texto': [texto]})
    print("\nOpciones para manipular el texto:")
    print("1. Contar palabras")
    print("2. Contar caracteres")
    print("3. Convertir a mayúsculas")
    print("4. Convertir a minúsculas")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        df['Cantidad de palabras'] = df['Texto'].apply(lambda x: len(x.split()))
        print(f"Cantidad de palabras: {df['Cantidad de palabras'][0]}")
    elif opcion == "2":
        df['CantidadEspacios'] = df['Texto'].apply(lambda x: len(x))
        df['CantidadSinEsp'] = df['Texto'].apply(lambda x: len(x.replace(" ", "")))
        print(f"Cantidad de caracteres con espacios: {df['CantidadEspacios'][0]}")
        print(f"Cantidad de caracteres sin espacios: {df['CantidadSinEsp'][0]}")
    elif opcion == "3":
        df['Texto en mayúsculas'] = df['Texto'].str.upper()
        print(f"Texto en mayúsculas: {df['Texto en mayúsculas'][0]}")
    elif opcion == "4":
        df['Texto en minúsculas'] = df['Texto'].str.lower()
        print(f"Texto en minúsculas: {df['Texto en minúsculas'][0]}")
    else:
        print("Opción no válida")