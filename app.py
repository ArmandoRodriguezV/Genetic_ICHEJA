from random import sample
from src.models.individual.individual import Individual
from src.models.environment.environment import Envioronment
from src.test.main_model_SQL import *

poblacion = [
    Individual(sample([f"R{i}" for i in range(1, 21)], 10)),
    Individual(sample([f"R{i}" for i in range(1, 21)], 10)),
    Individual(sample([f"R{i}" for i in range(1, 21)], 10)),
    Individual(sample([f"R{i}" for i in range(1, 21)], 10)),
    Individual(sample([f"R{i}" for i in range(1, 21)], 10))
]

# print(f"población inicial {len(poblacion)}")
# entorno = Envioronment(poblacion=poblacion, generations=2)
# entorno.start()

# entorno.print_pob(True)
# print(f"población final {len(entorno.poblacion)}")

mostrar_tabla_MRH()