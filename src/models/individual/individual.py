from typing import List
from ...test.main_model_SQL import hab, reactivos, mostrar_tabla_de

class Individual:
    def __init__(self, gens: List[str]):
        self.gens = gens
        self.habs_no_aprob = []
        self.habs_aprob = []
        self.habilidades_no_aprobadas()
        
        
        self.metric_1 = len(self.habs_no_aprob) / len(self.habs_aprob + self.habs_no_aprob)
        
    def habilidades_no_aprobadas(self):        
        for x in self.gens:
            for y in reactivos[x]:
                cal = hab[y]
                if cal < 0.7:
                    self.habs_no_aprob.append(cal)
                else:
                    self.habs_aprob.append(cal)
    
    def __str__(self):
        return mostrar_tabla_de(self.gens)