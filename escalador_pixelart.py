from PIL import Image, ImageEnhance
import os

def escalar_imagen(ruta_origen, factor_escala, ruta_destino):
    """
    Escala y aplica anti-aliasing a una imagen de pixel art.
    
    Args:
        ruta_origen (str): La ruta del archivo de imagen original.
        factor_escala (int): El factor por el cual se multiplicará el tamaño.
        ruta_destino (str): La ruta donde se guardará la nueva imagen escalada.
    """
    try:
        imagen = Image.open(ruta_origen)
        ancho, alto = imagen.size
        
        # 1. Escalar con el filtro NEAREST para mantener los píxeles
        nuevo_ancho_bruto = ancho * factor_escala
        nuevo_alto_bruto = alto * factor_escala
        
        imagen_pixelada = imagen.resize(
            (nuevo_ancho_bruto, nuevo_alto_bruto),
            resample=Image.NEAREST
        )
        
        # 2. Aplicar un segundo escalado con un filtro de alta calidad para el anti-aliasing
        imagen_suavizada = imagen_pixelada.resize(
            (int(nuevo_ancho_bruto * 1.5), int(nuevo_alto_bruto * 1.5)), # Pequeño extra para suavizar mejor
            resample=Image.LANCZOS # Este filtro es ideal para anti-aliasing
        )

        directorio_destino = os.path.dirname(ruta_destino)
        if not os.path.exists(directorio_destino):
            os.makedirs(directorio_destino)
            
        # Opcional: Aumentar el contraste ligeramente para que los colores resalten
        # enhancer = ImageEnhance.Contrast(imagen_suavizada)
        # imagen_final = enhancer.enhance(1.1)

        imagen_suavizada.save(ruta_destino)
        print(f"Imagen escalada y suavizada guardada en '{ruta_destino}'")

    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en '{ruta_origen}'. Asegúrate de haber ejecutado el script de dibujo primero.")
    except Exception as e:
        print(f"Ocurrió un error al escalar la imagen '{ruta_origen}': {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    
    # Lista de monstruos que se generarán
    lista_monstruos = [
        ("Dragón de la Llama", "Fuego"),
        ("Kraken del Océano", "Agua"),
        ("Coloso de Piedra", "Tierra"),
        ("Griffin Celestial", "Viento"),
        ("Arcángel Celestial", "Luz"),
        ("Dragón de las Sombras", "Oscuridad")
    ]

    # Define el factor de escala
    factor = 2
    
    # Define las carpetas
    carpeta_origen = "monstruos_dibujos"
    carpeta_destino = "monstruos_escalados"
    
    print(f"--- Escalando {len(lista_monstruos)} imágenes ---")
    
    for nombre_monstruo, tipo_monstruo in lista_monstruos:
        
        # Construye los nombres de archivo
        nombre_base = f"dibujo_avanzado_{nombre_monstruo.replace(' ', '_')}_{tipo_monstruo}.png"
        
        # Define las rutas
        ruta_origen = os.path.join(carpeta_origen, nombre_base)
        ruta_destino = os.path.join(carpeta_destino, nombre_base)
        
        # Llama a la función para escalar la imagen
        escalar_imagen(ruta_origen, factor, ruta_destino)
    
    print("--- Proceso de escalado completado ---")