from typing import List
from random import randint, random, sample, shuffle
from .individuo import Individuo
from .frame_generator import Frames
from .video import create_video
import csv

class Environment:
    def __init__(self, generations: int, poblacion: List[Individuo], pm: float = 1.0):
        self.generations = generations
        self.pm = pm
        self.poblacion = poblacion
        self.size = len(poblacion)
        
        self.console = False
        self.video = False
        
        self.all_best = []
        self.all_worsts = []
        self.all_averages = []
    
    def start(self):
        for i in range(self.generations):
            current = []
            h1, h2 = self.crosses()
            current.append(h1)
            current.append(h2)
            self.poblacion = self.poblacion + current
            
            self.pruning()
            self.analisis(i)
        
        if self.video:
            create_video()
        
        with open('logs.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.all_best)
            writer.writerow(self.all_averages)
            writer.writerow(self.all_worsts)
            
        
    def analisis(self, generation):
        copia = self.poblacion[:]
        copia = sorted(copia, key=lambda i: i.fitness, reverse=True)
        self.mejor = copia[0]
        self.peor = copia.pop()
        self.promedio = sum(ind.fitness for ind in self.poblacion) / len(self.poblacion)
        
        self.all_best.append(self.mejor.fitness)
        self.all_worsts.append(self.peor.fitness)
        self.all_averages.append(self.promedio)
        
        if self.console:
            print("============================================================================================================")
            print(f"Datos de población en generación {generation + 1}\n")
            print(f"peor {self.peor}")
            print(f"\n\tpromedio {self.promedio}\n")
            print(f"mejor {self.mejor} \n")
            print("============================================================================================================")
        
        if self.video:
            Frames(
                poblacion=self.poblacion,
                mejores=self.all_best,
                peores=self.all_worsts,
                promedio=self.all_averages,
                current=generation,
                generations=self.generations
            )

    def select_pair(self):
        p1, p2 = sample(range(len(self.poblacion)), 2)
        return self.poblacion[p1], self.poblacion[p2]
    
    def crosses(self):
        padre, madre = self.select_pair()
        point = randint(1, len(padre.gens) - 1)
        
        hijo1 = Individuo(padre.gens[:point] + madre.gens[point:])
        hijo2 = Individuo(madre.gens[:point] + padre.gens[point:])
        
        hijo1 = self.mutation(hijo1)
        hijo2 = self.mutation(hijo2)
        
        return hijo1, hijo2
        
    def mutation(self, hijo: Individuo):
        if random() < self.pm:    
            shuffle(hijo.gens)
            hijo.fitness_recalculate()
            hijo.nota = "Mutado shuffle"
        return hijo

    def pruning(self):
        self.poblacion = sorted(self.poblacion, key=lambda i: i.fitness, reverse=True)
        self.poblacion = self.poblacion[:self.size]

