from PIL import Image, ImageDraw
import os
import random

def crear_dibujo_base_monstruo(nombre_monstruo="Monstruo_Base", tamano=254):
    """
    Crea un dibujo de pixel art de un monstruo neutro en tonos de gris.
    """
    paleta_neutra = [(150, 150, 150), (100, 100, 100), (50, 50, 50), (200, 200, 200), (0, 0, 0)]

    imagen = Image.new('RGB', (tamano, tamano), paleta_neutra[1])
    dibujo = ImageDraw.Draw(imagen)

    # Dibuja la forma base del monstruo
    puntos_cuerpo = [(100, 100), (180, 100), (140, 60)]
    dibujo.polygon(puntos_cuerpo, fill=paleta_neutra[0], outline=paleta_neutra[2], width=2)
    dibujo.ellipse((100, 100, 180, 180), fill=paleta_neutra[0], outline=paleta_neutra[2], width=2)
    dibujo.line((140, 180, 140, 220), fill=paleta_neutra[2], width=4)
    dibujo.ellipse((120, 120, 130, 130), fill=paleta_neutra[4]) # Ojo
    dibujo.ellipse((150, 120, 160, 130), fill=paleta_neutra[4]) # Ojo

    # Sombreado y brillo
    dibujo.line((145, 125, 145, 135), fill=paleta_neutra[3], width=1)
    dibujo.line((165, 125, 165, 135), fill=paleta_neutra[3], width=1)
    
    nombre_archivo = f"{nombre_monstruo}.png"
    if not os.path.exists("monstruos_dibujos"):
        os.makedirs("monstruos_dibujos")
    ruta_guardado = os.path.join("monstruos_dibujos", nombre_archivo)
    imagen.save(ruta_guardado)
    print(f"Dibujo base de '{nombre_monstruo}' guardado en '{ruta_guardado}'")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    crear_dibujo_base_monstruo()