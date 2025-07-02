import os
import sys
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from typing import List
from .individuo import Individuo

class Frames:
    def __init__(self, poblacion: List[Individuo], mejores: List,
                 peores: List, promedio: List, current: int,
                 generations: int, inicio_global: float = time.time()):
        self.poblacion = poblacion
        self.mejores = mejores
        self.peores = peores
        self.promedio = promedio
        self.current = current
        self.generations = generations
        self.inicio_global = inicio_global
        
        self.generate_frame()

    def generate_hot_map_matrix(self):
        return [i.gens for i in self.poblacion]

    def generate_frame(self):
        porcentaje = int(((self.current + 1) / self.generations) * 100)
        total_bar = 30
        completado = int((porcentaje / 100) * total_bar)

        # ⌛ ETA: basado en tiempo promedio por generación
        elapsed = time.time() - self.inicio_global
        if self.current > 0:
            tiempo_promedio = elapsed / (self.current + 1)
            restante_estimado = tiempo_promedio * (self.generations - self.current - 1)
        else:
            restante_estimado = 0
        tiempo_formateado = str(datetime.timedelta(seconds=int(restante_estimado)))

        barra = f"Evolucionando {porcentaje:>3}% [{'=' * completado}{'-' * (total_bar - completado)}] {tiempo_formateado}"
        sys.stdout.write('\r' + barra)
        sys.stdout.flush()

        os.makedirs("frame", exist_ok=True)

        gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

        # 🔥 Heatmap
        ax0 = plt.subplot(gs[0])
        heatmap = ax0.imshow(self.generate_hot_map_matrix(), cmap="hot", interpolation="nearest", aspect='auto')
        ax0.set_title(f"Generación {self.current + 1}")
        plt.colorbar(heatmap, ax=ax0, label="Valor del gen")

        # 📈 Gráfica de evolución
        ax1 = plt.subplot(gs[1])
        generaciones = list(range(self.current + 1))
        ax1.plot(generaciones, self.mejores, label="Mejores", color="green")
        ax1.plot(generaciones, self.peores, label="Peores", color="red")
        ax1.plot(generaciones, self.promedio, label="Promedio", color="blue")
        ax1.set_xlabel("Generaciones")
        ax1.set_ylabel("Fitness")
        ax1.legend()
        ax1.grid(True)

        file_path = f"frame/frame_{self.current:04d}.png"
        plt.tight_layout()
        plt.savefig(file_path)
        plt.close()
