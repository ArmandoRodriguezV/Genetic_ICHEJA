from typing import List
from ..individual.individual import Individual

class Envioronment:
    
    def __init__(self, poblacion: List[Individual]):
        self.poblacion = poblacion
        
    