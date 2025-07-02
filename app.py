from src.environment import Environment
from src.individuo import Individuo

poblacion = [Individuo(num_gens=5) for _ in range(20)]
entorno = Environment(generations=500, poblacion=poblacion, pm=0.1)
entorno.video = True
entorno.start()