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
        self.metrica_1 = len(self.habs_no_aprob) / len(self.habs_aprob + self.habs_no_aprob)
        self.metrica_2 = sum([ reactivos_realizados[n] for n in self.gens])
        self.metrica_3 = len(self.habs_aprob)
        
        habilidades_totales = set()
        for r in self.gens:
            habilidades_totales.update(reactivos[r])
        self.metrica_4 = len(habilidades_totales)

        self.fitness = ((1 + self.metrica_1) * (1 + self.metrica_4)) / ((1 + self.metrica_2 ) * (1 + self.metrica_3))
        
        self.data = {
            "HNA": len(self.habs_no_aprob),
            "HA": len(self.habs_aprob),
            "Metricas": {
              "Metrica_1": self.metrica_1,
              "Metrica_2": self.metrica_2,
              "Metrica_3": self.metrica_3,
              "Metrica_4": self.metrica_4
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
            return f"{mostrar_tabla_de(self.gens)}\n Fitness: {self.fitness}\n Long: {len(self.gens)}"
        else:
            return f"Fitness: {self.fitness}\n Long: {len(self.gens)}"