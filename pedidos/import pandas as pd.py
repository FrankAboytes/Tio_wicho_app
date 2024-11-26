import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
tiempos = list(range(1, 51))  # Rango de 1 a 50
valores = [12, 13, 12, 11, 10, 13, 14, 13, 10, 11, 12, 14, 10, 11, 12, 9, 13, 10, 11, 10, 13, 12, 14, 13, 12, 15, 10, 11, 13, 12, 14, 10, 11, 13, 12, 13, 14, 15, 11, 12, 13, 11, 10, 12, 14, 13, 11, 10, 12, 9]
lci = 8  # Límite de control inferior constante
lcs = 16  # Límite de control superior constante
promedio = 12  # Línea promedio constante

# Crear el DataFrame
df = pd.DataFrame({
    'Tiempo': tiempos,
    'Valores': valores,
    'LCI': [lci] * len(tiempos),
    'LCS': [lcs] * len(tiempos),
    'Promedio': [promedio] * len(tiempos)
})

# Mostrar la tabla en la consola
print(df)

# Graficar el diagrama de control
plt.figure(figsize=(10, 6))
plt.plot(df['Tiempo'], df['Valores'], marker='o', label='Tiempos')
plt.plot(df['Tiempo'], df['LCI'], color='orange', label='LCI')
plt.plot(df['Tiempo'], df['LCS'], color='green', label='LCS')
plt.plot(df['Tiempo'], df['Promedio'], color='blue', label='Promedio')
plt.xlabel('Tiempo')
plt.ylabel('Valores')
plt.title('Diagrama de control')
plt.legend()
plt.grid()
plt.show()
