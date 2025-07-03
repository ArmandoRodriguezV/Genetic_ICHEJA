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
