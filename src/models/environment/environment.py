from random import sample, randint
from math import ceil
from typing import List
from ..individual.individual import Individual

class Envioronment:
    def __init__(self, poblacion: List[Individual], generations: int = 1):
        self.poblacion = poblacion
        self.generations = generations
        self.size = len(self.poblacion)
        
    def start(self):
        for _ in range(self.generations):
            self.crosses()
            self.poda()
    
    def select_pair(self):
        p1, p2 = sample(range(len(self.poblacion)), 2)
        return self.poblacion[p1], self.poblacion[p2]

    def crosses(self):
        new_children = []
        for _ in range(len(self.poblacion)):
            padre, madre = self.select_pair()
            point = randint(1, len(padre.gens) - 2)

            def cruzar(p1, p2):
                n = len(p1.gens)
                mitad = p1.gens[:point]
                resto = [g for g in p2.gens if g not in mitad]
                gens_hijo = (mitad + resto)[:n]
                return Individual(gens_hijo)

            h1 = cruzar(padre, madre)
            h2 = cruzar(madre, padre)

            new_children.append(h1)
            new_children.append(h2)

        self.poblacion.extend(new_children)
        
    def poda(self):
        self.poblacion = sorted(self.poblacion, key=lambda i: i.fitness, reverse=True)
        mejor_padre = self.poblacion[0]
        mejor_madre = self.poblacion[1]
        
        mitad_sin_padres = (len(self.poblacion) - 2)//2
        
        sub_1 = self.poblacion[2 + mitad_sin_padres:]
        sub_2 = self.poblacion[2 : mitad_sin_padres + 2]
        
        mitad_sub_grup = self.size / 2
        primera_mitad = sample(sub_1, ceil(mitad_sub_grup) - 2)
        segunda_mitad = sample(sub_2, int(mitad_sub_grup))
        
        self.poblacion.clear()
        self.poblacion.append(mejor_padre)
        self.poblacion.append(mejor_madre)
        self.poblacion += primera_mitad
        self.poblacion += segunda_mitad
        self.poblacion = sorted(self.poblacion, key=lambda i: i.fitness, reverse=True)

    def print_pob(self, show_table: bool = False):
        for i in self.poblacion:
            i.show_table = show_table
            print(i)
