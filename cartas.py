# cartas.py

class Monstruo:
    def __init__(self, nombre, tipo, ataque, defensa, imagen_path):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.posicion = 'ataque'
        self.imagen_path = imagen_path  # NUEVO: Atributo para la ruta de la imagen

    def cambiar_posicion(self):
        if self.posicion == 'ataque':
            self.posicion = 'defensa'
            print(f"{self.nombre} ha cambiado a posición de defensa.")
        else:
            self.posicion = 'ataque'
            print(f"{self.nombre} ha cambiado a posición de ataque.")

    def __str__(self):
        return (f"Monstruo: {self.nombre} (Tipo: {self.tipo})\n"
                f"  Ataque: {self.ataque}\n"
                f"  Defensa: {self.defensa}\n"
                f"  Posición: {self.posicion}")

    def mostrar_info(self):
        print(self)