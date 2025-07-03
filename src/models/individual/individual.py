from typing import List
from ...test.main_model_SQL import hab, reactivos, mostrar_tabla_de, reactivos_realizados

class Individual:
    def __init__(self, gens: List[str]):
        self.gens = gens
        self.show_table = False
        self.update_individual()
    
    def update_individual(self):
        self.habs_no_aprob = []
        self.habs_aprob = []
        self.habilidades_no_aprobadas()
        
        self.habs_no_aprob_por_r = []
        self.metrica_1 = round(len(self.habs_no_aprob) / len(self.habs_aprob + self.habs_no_aprob), 2)
        self.metrica_2 = sum([ reactivos_realizados[n] for n in self.gens])
        
        self.fitness = self.metrica_1 + self.metrica_2
        
        self.data = {
            "HNA": len(self.habs_no_aprob),
            "HA": len(self.habs_aprob),
            "Metricas": {
              "Metrica_1": self.metrica_1,
              "Metrica_2": self.metrica_2  
            },
            "Fitness": self.fitness
        }
        
    def habilidades_no_aprobadas(self):        
        for x in self.gens:
            for y in reactivos[x]:
                cal = hab[y]
                if cal < 0.7:
                    self.habs_no_aprob.append(y)
                else:
                    self.habs_aprob.append(y)
    
    def get_reactives(self):
        reactives = []
        for g in self.gens:
            reactives.append(reactivos[g])
        return reactivos
    
    def __str__(self):
        if self.show_table:
            return f"{self.mostrar_tabla_de(self.gens)}\nFitness: {self.fitness}"
        else:
            return f"Fitness: {self.fitness}"