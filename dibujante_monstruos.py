from PIL import Image, ImageDraw
import os

def crear_dibujo_monstruo(nombre_monstruo, tipo_monstruo, tamano=64):
    """
    Crea un dibujo de estilo 16-bit para un monstruo.

    Args:
        nombre_monstruo (str): El nombre del monstruo.
        tipo_monstruo (str): El tipo de elemento del monstruo (Fuego, Agua, etc.).
        tamano (int): El tamaño de la imagen final en píxeles (ej. 64x64).
        Debe ser un múltiplo de 16 para mantener el efecto de píxeles grandes.
    """
    # Escala base para mantener la estética de píxeles
    escala = tamano // 16
    
    # Asignar un color base según el tipo de monstruo
    colores_por_tipo = {
        'Fuego': (255, 69, 0),    # Naranja rojizo
        'Agua': (0, 191, 255),    # Azul claro
        'Tierra': (139, 69, 19),  # Marrón
        'Viento': (173, 216, 230), # Azul claro grisáceo
        'Luz': (255, 255, 0),      # Amarillo
        'Oscuridad': (75, 0, 130)  # Morado oscuro
    }
    color_base = colores_por_tipo.get(tipo_monstruo, (128, 128, 128)) # Gris por defecto
    
    # Crea una nueva imagen en blanco
    imagen = Image.new('RGB', (tamano, tamano), 'black')
    dibujo = ImageDraw.Draw(imagen)
    
    # Dibuja la forma principal del monstruo
    # Aquí puedes personalizar las formas para cada tipo de monstruo
    if tipo_monstruo == 'Fuego':
        # Dibuja una forma de flama
        dibujo.polygon(
            [
                (8 * escala, 15 * escala), (12 * escala, 10 * escala), 
                (15 * escala, 14 * escala), (10 * escala, 8 * escala), 
                (14 * escala, 5 * escala), (8 * escala, 0 * escala), 
                (2 * escala, 5 * escala), (6 * escala, 8 * escala), 
                (1 * escala, 14 * escala), (4 * escala, 10 * escala)
            ],
            fill=color_base
        )
    elif tipo_monstruo == 'Agua':
        # Dibuja una forma de gota
        dibujo.ellipse(
            (2 * escala, 2 * escala, 14 * escala, 14 * escala),
            fill=color_base
        )
        dibujo.polygon(
            [
                (8 * escala, 2 * escala), (10 * escala, 0 * escala), 
                (6 * escala, 0 * escala)
            ],
            fill=color_base
        )
    else:
        # Forma por defecto (cuadrado)
        dibujo.rectangle(
            (3 * escala, 3 * escala, 13 * escala, 13 * escala),
            fill=color_base
        )
        
    # Guarda la imagen
    nombre_archivo = f"dibujo_{nombre_monstruo.replace(' ', '_')}_{tipo_monstruo}.png"
    
    # Crea una carpeta 'monstruos_dibujos' si no existe
    if not os.path.exists("monstruos_dibujos"):
        os.makedirs("monstruos_dibujos")
        
    ruta_guardado = os.path.join("monstruos_dibujos", nombre_archivo)
    imagen.save(ruta_guardado)
    print(f"Dibujo de '{nombre_monstruo}' guardado en '{ruta_guardado}'")
    
# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Puedes generar dibujos para todos tus monstruos
    crear_dibujo_monstruo("Dragón de la Llama", "Fuego")
    crear_dibujo_monstruo("Kraken del Océano", "Agua")
    crear_dibujo_monstruo("Coloso de Piedra", "Tierra")
    crear_dibujo_monstruo("Griffin Celestial", "Viento")
    crear_dibujo_monstruo("Arcángel Celestial", "Luz")
    crear_dibujo_monstruo("Dragón de las Sombras", "Oscuridad")