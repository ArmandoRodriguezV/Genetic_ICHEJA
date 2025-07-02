import matplotlib.pyplot as plt
import csv

# Leer el CSV
datos = []
with open('logs.csv', 'r') as file:
    reader = csv.reader(file)
    for fila in reader:
        datos.append([float(x) for x in fila])

plt.figure(figsize=(16, 4))

for i, fila in enumerate(datos, start=1):
    plt.plot(fila, label=f'd{i}')

plt.title('Vectores registrados')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
