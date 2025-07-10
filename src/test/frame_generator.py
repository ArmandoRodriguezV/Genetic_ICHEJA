import matplotlib.pyplot as plt
import os

# Contador global para los frames
frame_counter = 0

def generate_frames(mejor, peor, promedio):
    global frame_counter

    # Asegurar que exista el directorio 'frames'
    os.makedirs("frames", exist_ok=True)

    # Crear la figura
    plt.figure(figsize=(10, 6))
    
    # Graficar las tres series
    plt.plot(mejor, label='Mejor', color='green')
    plt.plot(peor, label='Peor', color='red')
    plt.plot(promedio, label='Promedio', color='blue')

    # Agregar detalles al gráfico
    plt.title(f'Frame {frame_counter}')
    plt.xlabel('Iteración')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)

    # Guardar el frame como imagen
    frame_path = f"frames/frame_{frame_counter:04d}.png"
    plt.savefig(frame_path)
    plt.close()

    print(f"Frame guardado: {frame_path}")
    frame_counter += 1
