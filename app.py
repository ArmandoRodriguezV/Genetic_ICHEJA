from src.models.individual.individual import Individual
from src.test.main_model_SQL import hab, reactivos

i = Individual(['R1', 'R2', 'R9'])

print(i)
print(i.habs_no_aprob)
print(i.habs_aprob)