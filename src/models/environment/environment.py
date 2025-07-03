from random import sample
from typing import List
from ..individual.individual import Individual

class Envioronment:
    def __init__(self, poblacion: List[Individual]):
        self.poblacion = poblacion
        
    def start(self):
        for i in self.poblacion:
            current = []
            h1, h2 = self.crosses()
    
    def select_pair(self):
        p1, p2 = sample(range(len(self.poblacion)), 2)
        return self.poblacion[p1], self.poblacion[p2]
        
    def crosses(self):
        point = 1
        padre, madre = self.crosses()
        n = len(padre.gens)

        h1_start = padre.gens[:point]
        h1_rest = [g for g in madre.gens if g not in h1_start]
        h1 = (h1_start + h1_rest)[:n]

        h2_start = madre.gens[:point]
        h2_rest = [g for g in padre.gens if g not in h2_start]
        h2 = (h2_start + h2_rest)[:n]

        return Individual(h1), Individual(h2)

