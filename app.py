""" 
    El algoritmo funciona por medio de un entorno y un individuo
    El individuo se maneja por un genoma binario  

    # NOTA
    El algoritmo genera un analisis.csv que puede graficar el proceso
    
"""

from src.environment import Environment
from src.individuo import Individuo

poblacion = [Individuo(num_gens=5) for _ in range(20)]
entorno = Environment(generations=50, poblacion=poblacion, pm=0.7)


""" Imprime en consola mientras evoluciona  """
entorno.console = False

""" Genera un video 
    #Nota: 
    # suele tardar más
"""
entorno.video = False

entorno.start()