from src.models.individual.individual import Individual
from src.test.main_model_SQL import mostrar_tabla_completa

i = Individual(['R1', 'R2', 'R9'])

print(i.habs_no_aprob)
print(i.habs_aprob)
print(i.data)
print(i)

# mostrar_tabla_completa()