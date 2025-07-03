from tabulate import tabulate

hab = {
    "H1": 0.9,
    "H2": 1.0,
    "H3": 0.5,
    "H4": 0.0,
    "H5": 0.0,
    "H6": 0.0
}

reactivos = {
    "R1": ["H1", "H3", "H5"],
    "R2": ["H3", "H4"],
    "R3": ["H4", "H6"],
    "R4": ["H2", "H4", "H5"],
    "R5": ["H1", "H3", "H6"],
    "R6": ["H4", "H1"],
    "R7": ["H2", "H3", "H5"],
    "R8": ["H1", "H5", "H6"],
    "R9": ["H5", "H6"]
}
reactivos_realizados = {
    "R1": 2,
    "R2": 3,
    "R3": 0,
    "R4": 0,
    "R5": 0,
    "R6": 0,
    "R7": 0,
    "R8": 0,
    "R9": 1
}

todos_los_reactivos = {}
habilidades = list(hab.keys())

for r, hs in reactivos.items():
    todos_los_reactivos[r] = [1 if h in hs else 0 for h in habilidades]

def mostrar_tabla_de(lista_reactivos):
    habilidades_unicas = list(hab.keys())

    tabla = []
    for reactivo_key in lista_reactivos:
        if reactivo_key in reactivos:
            fila = []
            habilidades_en_reactivo = {h: hab[h] for h in reactivos[reactivo_key]}
            for habilidad in habilidades_unicas:
                valor = habilidades_en_reactivo.get(habilidad, -1)
                fila.append(valor)
            tabla.append([reactivo_key] + fila)

    headers = ["G"] + habilidades_unicas
    return tabulate(tabla, headers=headers, tablefmt="grid", floatfmt=".2f")

def mostrar_tabla_completa():
    habilidades_unicas = list(hab.keys())
    tabla = []
    for reactivo, hs in reactivos.items():
        fila = [1 if h in hs else 0 for h in habilidades_unicas]
        tabla.append([reactivo] + fila)
    headers = ["Reactivo"] + habilidades_unicas
    print(tabulate(tabla, headers=headers, tablefmt="grid"))