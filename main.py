# main.py

import os
import random
from cartas import Monstruo
# Importamos la función para colorear las imágenes
from coloreador_cartas import colorear_imagen

def inicializar_mazos():
    """
    Inicializa todos los mazos de monstruos y asigna una imagen coloreada.
    """
    print("Inicializando mazos...")
    
    # 1. Creamos las imágenes coloreadas para cada tipo de mazo
    ruta_imagen_base = os.path.join("monstruos_dibujos", "Monstruo_Base.png")
    if not os.path.exists(ruta_imagen_base):
        print("Error: El archivo 'Monstruo_Base.png' no existe. Por favor, ejecuta 'dibujante_monstruos.py' primero.")
        return {}

    rutas_imagenes = {
        'Fuego': colorear_imagen(ruta_imagen_base, 'Fuego'),
        'Agua': colorear_imagen(ruta_imagen_base, 'Agua'),
        'Tierra': colorear_imagen(ruta_imagen_base, 'Tierra'),
        'Viento': colorear_imagen(ruta_imagen_base, 'Viento'),
        'Luz': colorear_imagen(ruta_imagen_base, 'Luz'),
        'Oscuridad': colorear_imagen(ruta_imagen_base, 'Oscuridad'),
    }

    # 2. Inicializamos los monstruos y les asignamos la ruta de su imagen
    mazo_fuego = [
        Monstruo('Dragón de la Llama', 'Fuego', 40, 30, rutas_imagenes['Fuego']),
        Monstruo('Fénix de las Cenizas', 'Fuego', 35, 25, rutas_imagenes['Fuego']),
        Monstruo('Salamandra de Magma', 'Fuego', 30, 40, rutas_imagenes['Fuego']),
        Monstruo('Gigante de Lava', 'Fuego', 50, 20, rutas_imagenes['Fuego']),
        Monstruo('Eruptor', 'Fuego', 45, 30, rutas_imagenes['Fuego']),
        Monstruo('Quimera Ígnea', 'Fuego', 38, 38, rutas_imagenes['Fuego'])
    ]

    mazo_agua = [
        Monstruo('Kraken del Océano', 'Agua', 45, 35, rutas_imagenes['Agua']),
        Monstruo('Sirena de las Profundidades', 'Agua', 30, 45, rutas_imagenes['Agua']),
        Monstruo('Elementa Acuático', 'Agua', 35, 30, rutas_imagenes['Agua']),
        Monstruo('Hidra de Agua', 'Agua', 50, 25, rutas_imagenes['Agua']),
        Monstruo('Tritón Guerrero', 'Agua', 40, 40, rutas_imagenes['Agua']),
        Monstruo('Serpiente de Mar', 'Agua', 33, 33, rutas_imagenes['Agua'])
    ]

    mazo_tierra = [
        Monstruo('Coloso de Piedra', 'Tierra', 55, 25, rutas_imagenes['Tierra']),
        Monstruo('Ent Viviente', 'Tierra', 30, 50, rutas_imagenes['Tierra']),
        Monstruo('Guardían de la Montaña', 'Tierra', 40, 40, rutas_imagenes['Tierra']),
        Monstruo('Gólem de Barro', 'Tierra', 35, 35, rutas_imagenes['Tierra']),
        Monstruo('Bestia de Raíces', 'Tierra', 48, 28, rutas_imagenes['Tierra']),
        Monstruo('Roca Errante', 'Tierra', 25, 55, rutas_imagenes['Tierra'])
    ]
    
    mazo_viento = [
        Monstruo('Griffin Celestial', 'Viento', 42, 38, rutas_imagenes['Viento']),
        Monstruo('Ciclón Alado', 'Viento', 36, 42, rutas_imagenes['Viento']),
        Monstruo('Espíritu del Céfiro', 'Viento', 30, 30, rutas_imagenes['Viento']),
        Monstruo('Arpía de las Alturas', 'Viento', 50, 20, rutas_imagenes['Viento']),
        Monstruo('Silfo Aéreo', 'Viento', 28, 52, rutas_imagenes['Viento']),
        Monstruo('Tornado Encarnado', 'Viento', 45, 25, rutas_imagenes['Viento'])
    ]

    mazo_luz = [
        Monstruo('Arcángel Celestial', 'Luz', 40, 40, rutas_imagenes['Luz']),
        Monstruo('Guardián Sagrado', 'Luz', 35, 35, rutas_imagenes['Luz']),
        Monstruo('Elemental de Luz', 'Luz', 30, 50, rutas_imagenes['Luz']),
        Monstruo('León Solar', 'Luz', 50, 25, rutas_imagenes['Luz']),
        Monstruo('Radiante', 'Luz', 20, 60, rutas_imagenes['Luz']),
        Monstruo('Centinela Dorado', 'Luz', 48, 28, rutas_imagenes['Luz'])
    ]

    mazo_oscuridad = [
        Monstruo('Dragón de las Sombras', 'Oscuridad', 60, 20, rutas_imagenes['Oscuridad']),
        Monstruo('Espectro Nocturno', 'Oscuridad', 30, 30, rutas_imagenes['Oscuridad']),
        Monstruo('Golem de Obscuridad', 'Oscuridad', 35, 55, rutas_imagenes['Oscuridad']),
        Monstruo('Vampiro Sin Sombra', 'Oscuridad', 45, 35, rutas_imagenes['Oscuridad']),
        Monstruo('Pesadilla', 'Oscuridad', 25, 45, rutas_imagenes['Oscuridad']),
        Monstruo('Sombra Errante', 'Oscuridad', 38, 38, rutas_imagenes['Oscuridad'])
    ]
    
    return {
        'Fuego': mazo_fuego,
        'Agua': mazo_agua,
        'Tierra': mazo_tierra,
        'Viento': mazo_viento,
        'Luz': mazo_luz,
        'Oscuridad': mazo_oscuridad
    }

def main():
    print("--- Bienvenido a tu simulador de juego de cartas ---")
    mazos = inicializar_mazos()
    
    if not mazos:
        print("No se pudo iniciar el juego. Saliendo...")
        return

    # Ejemplo de cómo podrías usar las imágenes
    tipo_elegido = 'Fuego'
    mazo_jugador = mazos.get(tipo_elegido)
    if mazo_jugador:
        print(f"\nHas elegido el mazo de {tipo_elegido}.")
        
        # Muestra el primer monstruo del mazo, incluyendo la ruta de su imagen
        monstruo_ejemplo = mazo_jugador[0]
        print(f"\nAquí está tu primer monstruo:\n{monstruo_ejemplo}")
        print(f"Su imagen se encuentra en la ruta: {monstruo_ejemplo.imagen_path}")

    print("\n--- ¡Juego terminado! ---")


if __name__ == "__main__":
    # Asegúrate de haber ejecutado estos scripts antes:
    # 1. python dibujante_monstruos.py
    # 2. python coloreador_cartas.py
    main()