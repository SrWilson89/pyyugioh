from PIL import Image, ImageDraw
import os
import random

def crear_dibujo_avanzado(nombre_monstruo, tipo_monstruo, tamano=128):
    """
    Crea un dibujo de estilo pixel art para un monstruo con reglas complejas,
    sombreado y un fondo temático.
    """
    paletas_por_tipo = {
        'Fuego': [(255, 69, 0), (255, 140, 0), (255, 215, 0), (255, 255, 255)],
        'Agua': [(0, 191, 255), (30, 144, 255), (0, 0, 255), (240, 248, 255)],
        'Tierra': [(139, 69, 19), (160, 82, 45), (101, 67, 33), (255, 255, 255)],
        'Viento': [(173, 216, 230), (135, 206, 250), (100, 149, 237), (255, 255, 255)],
        'Luz': [(255, 255, 0), (255, 255, 153), (255, 250, 205), (255, 255, 255)],
        'Oscuridad': [(75, 0, 130), (128, 0, 128), (25, 25, 112), (0, 0, 0)]
    }
    colores = paletas_por_tipo.get(tipo_monstruo, [(128, 128, 128), (169, 169, 169), (105, 105, 105), (255, 255, 255)])
    
    imagen = Image.new('RGB', (tamano, tamano), 'black')
    dibujo = ImageDraw.Draw(imagen)
    
    # Dibuja el fondo
    def dibujar_fondo():
        if tipo_monstruo == 'Fuego':
            # Fondo de volcán
            dibujo.rectangle((0, 0, tamano, tamano), fill=(0, 0, 0))
            dibujo.polygon([(0, tamano), (tamano//2, tamano//4), (tamano, tamano)], fill=(50, 50, 50))
            dibujo.ellipse((tamano//2 - 10, tamano//4 - 10, tamano//2 + 10, tamano//4 + 10), fill=colores[0])
        elif tipo_monstruo == 'Agua':
            # Fondo de lecho marino
            dibujo.rectangle((0, 0, tamano, tamano), fill=colores[1])
            dibujo.rectangle((0, tamano-20, tamano, tamano), fill=(101, 67, 33))
        elif tipo_monstruo == 'Tierra':
            # Fondo de cueva con cristales
            dibujo.rectangle((0, 0, tamano, tamano), fill=(50, 50, 50))
            dibujo.polygon([(30, 30), (50, 10), (70, 30)], fill=colores[0])
            dibujo.polygon([(80, 50), (100, 40), (90, 60)], fill=colores[1])
        elif tipo_monstruo == 'Viento':
            # Fondo de cielo nublado
            dibujo.rectangle((0, 0, tamano, tamano), fill=colores[1])
            dibujo.ellipse((-20, 20, 50, 70), fill=colores[3])
            dibujo.ellipse((60, 40, 130, 90), fill=colores[3])
        elif tipo_monstruo == 'Luz':
            # Fondo de sol
            dibujo.rectangle((0, 0, tamano, tamano), fill=colores[1])
            dibujo.ellipse((tamano//4, tamano//4, tamano*3//4, tamano*3//4), fill=colores[0])
        elif tipo_monstruo == 'Oscuridad':
            # Fondo de noche estrellada
            dibujo.rectangle((0, 0, tamano, tamano), fill=colores[3])
            for _ in range(20):
                x = random.randint(0, tamano)
                y = random.randint(0, tamano)
                dibujo.point((x, y), fill=colores[0])
    
    # Dibuja la forma del monstruo
    def dibujar_monstruo():
        if tipo_monstruo == 'Fuego':
            # Cuerpo de dragón con sombreado
            dibujo.polygon([(30, 40), (100, 50), (100, 100), (30, 90)], fill=colores[0])
            dibujo.polygon([(40, 50), (90, 60), (90, 90), (40, 80)], fill=colores[1])
            dibujo.polygon([(45, 55), (85, 65), (85, 85), (45, 75)], fill=colores[2])
            # Cuello y cabeza
            dibujo.polygon([(40, 50), (60, 30), (80, 40)], fill=colores[1])
            dibujo.ellipse((70, 20, 90, 40), fill=colores[1])
            # Ala
            dibujo.polygon([(50, 40), (120, 20), (110, 80)], fill=colores[2])
            dibujo.line((50, 40, 85, 45), fill=colores[3], width=2)
        elif tipo_monstruo == 'Agua':
            # Cuerpo de kraken con sombreado
            dibujo.ellipse((30, 30, 90, 90), fill=colores[0])
            dibujo.ellipse((35, 35, 85, 85), fill=colores[1])
            # Tentáculos
            dibujo.line((60, 90, 40, 120), fill=colores[1], width=5)
            dibujo.line((60, 90, 80, 120), fill=colores[1], width=5)
            dibujo.line((60, 90, 90, 110), fill=colores[1], width=5)
        elif tipo_monstruo == 'Tierra':
            # Gólem de roca con sombreado
            dibujo.rectangle((40, 50, 80, 110), fill=colores[0])
            dibujo.rectangle((30, 40, 90, 50), fill=colores[1])
            dibujo.rectangle((50, 20, 70, 40), fill=colores[0])
            dibujo.rectangle((40, 25, 60, 35), fill=colores[1])
        elif tipo_monstruo == 'Viento':
            # Cuerpo de grifo con sombreado
            dibujo.polygon([(40, 60), (80, 60), (60, 30)], fill=colores[0])
            dibujo.polygon([(60, 30), (20, 10), (50, 50)], fill=colores[1])
            dibujo.polygon([(60, 30), (100, 10), (70, 50)], fill=colores[1])
            dibujo.line((60, 60, 60, 90), fill=colores[2], width=3)
        elif tipo_monstruo == 'Luz':
            # Ángel con sombreado
            dibujo.ellipse((50, 40, 80, 80), fill=colores[0])
            dibujo.line((65, 80, 65, 110), fill=colores[1], width=5)
            dibujo.polygon([(45, 60), (20, 40), (40, 80)], fill=colores[2])
            dibujo.polygon([(85, 60), (110, 40), (90, 80)], fill=colores[2])
        elif tipo_monstruo == 'Oscuridad':
            # Demonio con sombreado
            dibujo.polygon([(50, 50), (70, 50), (60, 20)], fill=colores[0])
            dibujo.ellipse((40, 60, 80, 100), fill=colores[1])
            dibujo.polygon([(50, 60), (30, 40), (45, 70)], fill=colores[2])
            dibujo.polygon([(70, 60), (90, 40), (75, 70)], fill=colores[2])
    
    dibujar_fondo()
    dibujar_monstruo()

    nombre_archivo = f"dibujo_avanzado_{nombre_monstruo.replace(' ', '_')}_{tipo_monstruo}.png"
    if not os.path.exists("monstruos_dibujos"):
        os.makedirs("monstruos_dibujos")
    ruta_guardado = os.path.join("monstruos_dibujos", nombre_archivo)
    imagen.save(ruta_guardado)
    print(f"Dibujo de '{nombre_monstruo}' guardado en '{ruta_guardado}'")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    crear_dibujo_avanzado("Dragón de la Llama", "Fuego")
    crear_dibujo_avanzado("Kraken del Océano", "Agua")
    crear_dibujo_avanzado("Coloso de Piedra", "Tierra")
    crear_dibujo_avanzado("Griffin Celestial", "Viento")
    crear_dibujo_avanzado("Arcángel Celestial", "Luz")
    crear_dibujo_avanzado("Dragón de las Sombras", "Oscuridad")