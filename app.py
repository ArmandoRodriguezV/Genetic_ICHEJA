from random import sample
from src.models.individual.individual import Individual
from src.models.environment.environment import Envioronment
from src.test.main_model_SQL import mostrar_tabla_completa, reactivos

poblacion = []

claves_reactivos = list(reactivos.keys())

for _ in range(20):
    seleccionados = sample(claves_reactivos, 10)
    individuo = Individual(seleccionados)
    poblacion.append(individuo)

# Mostrar los genes de cada individuo
for i, ind in enumerate(poblacion):
    print(f"Individuo {i+1}: {ind.gens}")
