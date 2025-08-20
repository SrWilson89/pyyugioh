import random

class Monstruo:
    """
    Representa a una carta de monstruo en el juego.
    """
    def __init__(self, nombre, tipo, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.posicion = 'ataque'
        self.has_attacked = False

    def __repr__(self):
        return f'{self.nombre} ({self.tipo}) - ATK:{self.ataque} DEF:{self.defensa}'

class Jugador:
    """
    Representa a un jugador en el juego.
    """
    def __init__(self, nombre, mazo):
        self.nombre = nombre
        self.puntos_vida = 30
        self.mazo = mazo
        self.mano = []
        self.campo = []
        self.descartes = []

    def robar_carta(self):
        """
        Roba una carta del mazo y la añade a la mano.
        """
        if self.mazo:
            carta_robada = self.mazo.pop(0)
            self.mano.append(carta_robada)
            print(f'{self.nombre} robó {carta_robada.nombre}.')
            if len(self.mano) > 5:
                print(f'La mano de {self.nombre} está llena. ¡Debes descartar una carta!')
                descartada = self.mano.pop()
                self.descartes.append(descartada)
                print(f'{self.nombre} descartó {descartada.nombre}.')

    def invocar_monstruo(self, indice_carta, posicion):
        """
        Invoca un monstruo de la mano al campo.
        'indice_carta' es el índice de la carta en la mano del jugador.
        """
        if not (0 <= indice_carta < len(self.mano)):
            print("Índice de carta no válido.")
            return False
        
        if len(self.campo) >= 3:
            print("No se puede invocar más monstruos. El campo está lleno.")
            return False

        monstruo_a_invocar = self.mano.pop(indice_carta)
        monstruo_a_invocar.posicion = posicion
        self.campo.append(monstruo_a_invocar)
        print(f'{self.nombre} invocó a {monstruo_a_invocar.nombre} en posición de {posicion}.')
        return True