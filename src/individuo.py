import random

class Individuo:
    def __init__(self, gens = None, num_gens: int = 5):
        if gens is None:
            gens = [random.randint(0, 1) for _ in range(num_gens)]
        if num_gens < 2:
            self.gens = 2
        else:
            self.gens = gens
        self.fitness = int("".join(map(str, self.gens)), 2)
        self.nota = ""
    
    def fitness_recalculate(self):
        self.fitness = int("".join(map(str, self.gens)), 2)
    
    def __str__(self):
        return f"individuo: {self.gens} \nfitness: {self.fitness}\n {self.nota}"