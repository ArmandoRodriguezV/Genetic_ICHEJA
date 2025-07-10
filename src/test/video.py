import cv2
import os
import sys
import time
import datetime

def create_video(
    inicio_global:float = time.time()
):
    # 📁 Ruta de las imágenes
    carpeta_imagenes = './frames'
    imagenes = sorted([img for img in os.listdir(carpeta_imagenes) if img.endswith(('.png', '.jpg'))])

    if not imagenes:
        print("❌ No se encontraron imágenes en la carpeta.")
        return

    # 📏 Obtener dimensiones de la primera imagen
    frame_ejemplo = cv2.imread(os.path.join(carpeta_imagenes, imagenes[0]))
    alto, ancho, _ = frame_ejemplo.shape

    # 🎬 Crear el video
    fps = 10  # fotogramas por segundo
    salida = cv2.VideoWriter('video_resultado.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (ancho, alto))

    total = len(imagenes)
    barra_largo = 60
    inicio_global = inicio_global

    for i, imagen in enumerate(imagenes):
        frame = cv2.imread(os.path.join(carpeta_imagenes, imagen))
        salida.write(frame)

        # 🧮 Cálculo del ETA
        elapsed = time.time() - inicio_global
        porcentaje = int(((i + 1) / total) * 100)
        completado = int((porcentaje / 100) * barra_largo)

        if i > 0:
            tiempo_promedio = elapsed / (i + 1)
            restante_estimado = tiempo_promedio * (total - i - 1)
        else:
            restante_estimado = 0

        tiempo_formateado = str(datetime.timedelta(seconds=int(restante_estimado)))
        barra = f"Render {porcentaje:>3}% [{'=' * completado}{'-' * (barra_largo - completado)}] {tiempo_formateado}"

        sys.stdout.write('\r' + barra)
        sys.stdout.flush()

    salida.release()
    print("\n✅ Video creado exitosamente.")
