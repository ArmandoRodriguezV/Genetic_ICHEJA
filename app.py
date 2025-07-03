from src.models.individual.individual import Individual
from src.models.environment.environment import Envioronment
from src.test.main_model_SQL import mostrar_tabla_completa

poblacion = [
    Individual(['R1', 'R2', 'R9']),
    Individual(['R2', 'R3', 'R4']),
    Individual(['R2', 'R4', 'R5']),
    Individual(['R1', 'R2', 'R4']),
    Individual(['R1', 'R5', 'R9'])
]

environment = Envioronment(poblacion)

h1, h2 = environment.cross(padre=poblacion[0], madre=poblacion[1])

print(h1)
print(h2)

# mostrar_tabla_completa()