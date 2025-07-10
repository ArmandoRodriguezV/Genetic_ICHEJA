from src.models.individual.individual import Individual
from src.models.environment.environment import Envioronment
from src.test.main_model_SQL import *
from src.test.individual_models import poblacion_1

entorno = Envioronment(poblacion_1, generations=100, pm=0.1)

entorno.generate_video()
entorno.start()

entorno.show_poblation(True)