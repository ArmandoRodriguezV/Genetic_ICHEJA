from random import sample
from src.models.individual.individual import Individual
from src.models.environment.environment import Envioronment
from src.test.main_model_SQL import mostrar_tabla_MRH, MRH
from src.test.validation import (validar_estrategia, validar_poblacion, crear_mrh_temp, mostrar_reporte_validacion)

def main():
    print("=== MATRIZ MRH ORIGINAL ===")
    mostrar_tabla_MRH()

    MRH_temp = MRH.copy()

    print("\n=== CREANDO POBLACIÓN INICIAL ===")
    poblacion_inicial = []
    for i in range(8):
        genes = sample(list(MRH.keys()), 3)
        individuo = Individual(genes)
        poblacion_inicial.append(individuo)

    ambiente = Envioronment(poblacion_inicial, generations=3)

    print(f"\nPoblación inicial creada con {len(poblacion_inicial)} individuos")
    print("Fitness inicial:")
    for i, individuo in enumerate(poblacion_inicial):
        print(f"  Individuo {i+1}: {individuo.gens} - Fitness: {individuo.fitness:.4f}")

    print("\n=== EJECUTANDO ALGORITMO GENÉTICO ===")
    print(f"Ejecutando {ambiente.generations} generaciones...")
    ambiente.start()

    print(f"\nPoblación final: {len(ambiente.poblacion)} individuos")
    
    print("\n=== MEJORES INDIVIDUOS DE LA POBLACIÓN FINAL ===")
    poblacion_ordenada = sorted(ambiente.poblacion, key=lambda x: x.fitness, reverse=True)
    for i, individuo in enumerate(poblacion_ordenada[:5]):
        print(f"{i+1}. Genes: {individuo.gens} - Fitness: {individuo.fitness:.4f}")

    print("\n" + "="*60)
    print("APLICANDO ESTRATEGIA DE VALIDACIÓN")
    print("="*60)

    print("\n--- VALIDACIÓN DEL MEJOR INDIVIDUO ---")
    mejor_individuo = max(ambiente.poblacion, key=lambda x: x.fitness)
    print(f"Mejor individuo actual: {mejor_individuo.gens} (Fitness: {mejor_individuo.fitness:.4f})")
    
    resultado_mejor = validar_estrategia(mejor_individuo, mostrar_detalle=True)

    print("\n" + "-"*60)
    print("VALIDACIÓN DE TODA LA POBLACIÓN")
    print("-"*60)
    
    resultados_poblacion = validar_poblacion(ambiente, mostrar_mejores=5)

    mostrar_reporte_validacion(resultados_poblacion, mostrar_analisis=True)

    print("\n" + "-"*60)
    print("CREANDO MRH_TEMP PARA EL MEJOR INDIVIDUO")
    print("-"*60)
    
    mejor_validado = max(resultados_poblacion, key=lambda x: x["despues"]["fitness"])
    mejor_individuo_validado = mejor_validado["individuo"]
    
    print(f"Mejor individuo después de validación: {mejor_individuo_validado.gens}")
    print(f"Fitness potencial: {mejor_validado['despues']['fitness']:.4f}")
    
    MRH_temp_final = crear_mrh_temp(mejor_individuo_validado)
    
    print("\nMRH_temp creado para el mejor individuo validado")
    print("Este MRH_temp contiene las calificaciones aprobatorias simuladas")

    print("\n" + "-"*60)
    print("DEMOSTRACIÓN CON EJEMPLOS ESPECÍFICOS")
    print("-"*60)
    
    print("\n--- Ejemplo 1: Individuo con habilidades no aprobadas ---")
    individual_demo1 = Individual(["R1", "R2", "R9"])
    validar_estrategia(individual_demo1, mostrar_detalle=True)
    
    print("\n--- Ejemplo 2: Individuo con habilidades mayormente aprobadas ---")
    individual_demo2 = Individual(["R4", "R5", "R13"])
    validar_estrategia(individual_demo2, mostrar_detalle=True)

    print("\n" + "="*60)
    print("RESUMEN FINAL")
    print("="*60)
    
    print(f"Población inicial: {len(poblacion_inicial)} individuos")
    print(f"Población final: {len(ambiente.poblacion)} individuos")
    print(f"Mejor fitness original: {max(ambiente.poblacion, key=lambda x: x.fitness).fitness:.4f}")
    print(f"Mejor fitness después de validación: {mejor_validado['despues']['fitness']:.4f}")
    print(f"Mejora potencial: {mejor_validado['mejora_fitness']:+.4f}")
    
    print(f"\nLa estrategia de validación muestra que el individuo:")
    print(f"  {mejor_individuo_validado.gens}")
    print(f"  Tiene el mayor potencial de mejora si se resuelven correctamente")
    print(f"  sus reactivos asociados.")

if __name__ == "__main__":
    main()