from PIL import Image
import os

def colorear_imagen(ruta_origen, tipo_monstruo):
    """
    Toma una imagen base y la colorea según un tipo de elemento.
    """
    paletas_color = {
        'Fuego': (255, 100, 0),
        'Agua': (0, 150, 255),
        'Tierra': (139, 69, 19),
        'Viento': (173, 216, 230),
        'Luz': (255, 255, 0),
        'Oscuridad': (75, 0, 130),
        'Planta': (50, 205, 50),
        'Eléctrico': (255, 255, 50)
    }

    color_base = paletas_color.get(tipo_monstruo, (150, 150, 150))
    
    try:
        imagen = Image.open(ruta_origen).convert("RGB")
        pixeles = imagen.load()
        ancho, alto = imagen.size

        for x in range(ancho):
            for y in range(alto):
                r, g, b = pixeles[x, y]
                # Aplicamos el filtro de color si el píxel no es negro (contorno)
                if r != 0 or g != 0 or b != 0:
                    promedio = (r + g + b) // 3
                    nuevo_r = int(color_base[0] * (promedio / 255.0))
                    nuevo_g = int(color_base[1] * (promedio / 255.0))
                    nuevo_b = int(color_base[2] * (promedio / 255.0))
                    pixeles[x, y] = (nuevo_r, nuevo_g, nuevo_b)
        
        carpeta_destino = os.path.join("monstruos_coloreados", tipo_monstruo)
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            
        nombre_archivo = f"monstruo_{tipo_monstruo}.png"
        ruta_guardado = os.path.join(carpeta_destino, nombre_archivo)
        imagen.save(ruta_guardado)
        
        print(f"Imagen para el mazo '{tipo_monstruo}' guardada en '{ruta_guardado}'")
        return ruta_guardado
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_origen}'.")
        return None

if __name__ == "__main__":
    tipos_mazos = ['Fuego', 'Agua', 'Tierra', 'Viento', 'Luz', 'Oscuridad']
    ruta_base = os.path.join("monstruos_dibujos", "Monstruo_Base.png")
    for tipo in tipos_mazos:
        colorear_imagen(ruta_base, tipo)