import pandas as pd
import matplotlib.pyplot as plt

def graficar_senales_csv(DS0005_CSV):
    # Leer el CSV desde la línea 28 (línea 27 en índice 0)
    datos = pd.read_csv('DS0005.CSV', skiprows=27)

    # Mostrar las primeras filas para entender la estructura
    print("Columnas detectadas:", datos.columns.tolist())
    print(datos.head())

    # Suponiendo que la primera columna es tiempo y las siguientes son canales de voltaje
    tiempo = datos.iloc[:, 0]
    señales = datos.iloc[:, 1:]

    # Graficar cada señal
    plt.figure(figsize=(10, 6))
    for columna in señales.columns:
        plt.plot(tiempo, señales[columna], label=columna)

    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.title("Señales del Osciloscopio")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Llama a la función con la ruta del archivo CSV
graficar_senales_csv("ruta/a/tu/archivo.csv")
