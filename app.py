from src.models.individual.individual import Individual
from src.models.environment.environment import Envioronment
from src.test.main_model_SQL import mostrar_tabla_completa, reactivos

i1 = Individual(["R2", "R9", "R5"])

print(i1.data)

mostrar_tabla_completa()