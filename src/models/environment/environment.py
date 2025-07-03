from random import sample, randint
from typing import List
from ..individual.individual import Individual

class Envioronment:
    def __init__(self, poblacion: List[Individual], generations: int = 1):
        self.poblacion = poblacion
        self.generations = generations
        
    def start(self):
        for _ in range(self.generations):
            self.crosses()
    
    def select_pair(self):
        p1, p2 = sample(range(len(self.poblacion)), 2)
        return self.poblacion[p1], self.poblacion[p2]

    def crosses(self):
        for _ in range(len(self.poblacion)):
            padre, madre = self.select_pair()
            point = 5
            
            h1 = Individual(padre.gens[:point] + madre.gens[point:])
            h2 = Individual(madre.gens[:point] + padre.gens[point:])
            
            self.poblacion.append(h1)
            self.poblacion.append(h2)
        
    def print_pob(self, show_table: bool):
        for i in self.poblacion:
            i.show_table = show_table
            print(i)


