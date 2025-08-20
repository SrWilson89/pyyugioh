import random
from cartas import Monstruo, Jugador

def inicializar_mazos():
    """
    Función para crear y devolver una lista de todos los mazos.
    (Código del mazo de Fuego completo, como el ejemplo anterior)
    """
    mazo_fuego = [
        Monstruo('Dragón de la Llama', 'Fuego', 40, 30),
        Monstruo('Fénix de las Cenizas', 'Fuego', 35, 25),
        Monstruo('Salamandra de Magma', 'Fuego', 30, 20),
        Monstruo('Espíritu de Brasas', 'Fuego', 25, 15),
        Monstruo('Gólem de Lava', 'Fuego', 30, 40),
        Monstruo('Demonio de Ceniza', 'Fuego', 45, 10),
        Monstruo('Elementalista Ígneo', 'Fuego', 20, 20),
        Monstruo('Llama Errante', 'Fuego', 15, 15),
        Monstruo('Tritón de Fuego', 'Fuego', 25, 30),
        Monstruo('Ciclón de Fuego', 'Fuego', 35, 30),
        Monstruo('Centinela de Roca Fundida', 'Fuego', 20, 35),
        Monstruo('Explosión Solar', 'Fuego', 40, 10),
        Monstruo('Guardián del Sol', 'Fuego', 30, 35),
        Monstruo('Serpiente de Humo', 'Fuego', 20, 25),
        Monstruo('Mago Pirotécnico', 'Fuego', 30, 15),
        Monstruo('Criatura de Cobre', 'Fuego', 10, 50),
        Monstruo('Anillo de Fuego', 'Fuego', 20, 20),
        Monstruo('León de Fuego', 'Fuego', 35, 30),
        Monstruo('Escudo de Fuego', 'Fuego', 10, 45),
        Monstruo('Espada de la Llama', 'Fuego', 25, 25),
    ]

    mazo_agua = [
        Monstruo('Leviatán Abisal', 'Agua', 35, 40),
        Monstruo('Kraken del Océano', 'Agua', 40, 30),
        Monstruo('Sirena de las Profundidades', 'Agua', 25, 30),
        Monstruo('Tritón de las Corrientes', 'Agua', 30, 25),
        Monstruo('Gólem de Hielo', 'Agua', 30, 45),
        Monstruo('Tsunami Devastador', 'Agua', 45, 15),
        Monstruo('Némesis Marina', 'Agua', 20, 35),
        Monstruo('Marea Tempestuosa', 'Agua', 15, 20),
        Monstruo('Ballena Colosal', 'Agua', 40, 35),
        Monstruo('Tifón Acuático', 'Agua', 35, 30),
        Monstruo('Guardian de los Mares', 'Agua', 25, 40),
        Monstruo('Cascada Imparable', 'Agua', 40, 15),
        Monstruo('Serpiente Marina', 'Agua', 30, 30),
        Monstruo('Nébeda Acuática', 'Agua', 20, 30),
        Monstruo('Hechicero de las Mareas', 'Agua', 30, 20),
        Monstruo('Coraza de Perla', 'Agua', 15, 50),
        Monstruo('Vórtice Acuático', 'Agua', 25, 25),
        Monstruo('Hipocampo Real', 'Agua', 35, 30),
        Monstruo('Escudo de Coral', 'Agua', 10, 50),
        Monstruo('Tridente Abisal', 'Agua', 30, 25),
    ]

    mazo_tierra = [
        Monstruo('Coloso de Piedra', 'Tierra', 30, 50),
        Monstruo('Gólem de Granito', 'Tierra', 35, 45),
        Monstruo('Dragón de Montaña', 'Tierra', 40, 35),
        Monstruo('Guardian de las Cavernas', 'Tierra', 25, 40),
        Monstruo('Titan de Roca', 'Tierra', 30, 50),
        Monstruo('Terremoto Viviente', 'Tierra', 45, 20),
        Monstruo('Elementalista Terrestre', 'Tierra', 20, 35),
        Monstruo('Avalancha', 'Tierra', 20, 25),
        Monstruo('Mastodonte Prehistórico', 'Tierra', 35, 40),
        Monstruo('Deslizamiento de Tierra', 'Tierra', 30, 35),
        Monstruo('Centinela de Cristal', 'Tierra', 25, 45),
        Monstruo('Meteoro Terrestre', 'Tierra', 40, 25),
        Monstruo('Protector del Bosque', 'Tierra', 30, 40),
        Monstruo('Gusano de Arena', 'Tierra', 25, 30),
        Monstruo('Druida de la Tierra', 'Tierra', 30, 30),
        Monstruo('Fortaleza Viviente', 'Tierra', 15, 60),
        Monstruo('Anillo de Piedra', 'Tierra', 25, 30),
        Monstruo('León de Montaña', 'Tierra', 35, 35),
        Monstruo('Muro de Granito', 'Tierra', 10, 55),
        Monstruo('Martillo Telúrico', 'Tierra', 35, 30),
    ]

    mazo_viento = [
        Monstruo('Dragón de Tormenta', 'Viento', 45, 25),
        Monstruo('Fénix de los Vientos', 'Viento', 40, 20),
        Monstruo('Harpía Tempestuosa', 'Viento', 35, 15),
        Monstruo('Espíritu del Viento', 'Viento', 30, 10),
        Monstruo('Gólem de Nubes', 'Viento', 25, 35),
        Monstruo('Tifón Devastador', 'Viento', 50, 5),
        Monstruo('Elementalista Aéreo', 'Viento', 25, 20),
        Monstruo('Ráfaga Veloz', 'Viento', 20, 10),
        Monstruo('Griffin Celestial', 'Viento', 40, 25),
        Monstruo('Tornado', 'Viento', 35, 20),
        Monstruo('Centinela de la Tormenta', 'Viento', 20, 30),
        Monstruo('Rayo Huracanado', 'Viento', 45, 10),
        Monstruo('Guardián de los Cielos', 'Viento', 30, 25),
        Monstruo('Serpiente de Viento', 'Viento', 25, 15),
        Monstruo('Mago de la Tempestad', 'Viento', 35, 10),
        Monstruo('Ciclón Etéreo', 'Viento', 15, 40),
        Monstruo('Vórtice de Aire', 'Viento', 25, 20),
        Monstruo('Águila Real', 'Viento', 40, 20),
        Monstruo('Escudo de Viento', 'Viento', 15, 35),
        Monstruo('Espada de la Tempestad', 'Viento', 30, 15),
    ]

    mazo_luz = [
        Monstruo('Arcángel Celestial', 'Luz', 35, 40),
        Monstruo('Unicornio Divino', 'Luz', 30, 35),
        Monstruo('Dragón de Luz', 'Luz', 40, 30),
        Monstruo('Espíritu de Pureza', 'Luz', 25, 30),
        Monstruo('Gólem de Cristal', 'Luz', 30, 45),
        Monstruo('Rayo Solar', 'Luz', 45, 20),
        Monstruo('Sacerdote de la Luz', 'Luz', 20, 35),
        Monstruo('Resplandor', 'Luz', 15, 25),
        Monstruo('Pegaso Brillante', 'Luz', 35, 30),
        Monstruo('Estallido de Luz', 'Luz', 40, 25),
        Monstruo('Centinela Sagrado', 'Luz', 25, 40),
        Monstruo('Destello Cegador', 'Luz', 40, 15),
        Monstruo('Guardián Divino', 'Luz', 30, 35),
        Monstruo('Serafín', 'Luz', 25, 30),
        Monstruo('Mago de la Claridad', 'Luz', 30, 25),
        Monstruo('Escudo de Fe', 'Luz', 15, 50),
        Monstruo('Aura Sagrada', 'Luz', 25, 30),
        Monstruo('León Alado', 'Luz', 35, 30),
        Monstruo('Barrera de Luz', 'Luz', 10, 45),
        Monstruo('Espada del Amanecer', 'Luz', 35, 25),
    ]

    mazo_oscuridad = [
        Monstruo('Dragón de las Sombras', 'Oscuridad', 45, 25),
        Monstruo('Demonio del Abismo', 'Oscuridad', 40, 20),
        Monstruo('Espectro Nocturno', 'Oscuridad', 30, 15),
        Monstruo('Espíritu de la Noche', 'Oscuridad', 25, 10),
        Monstruo('Gólem de Obsidiana', 'Oscuridad', 35, 40),
        Monstruo('Pesadilla Viviente', 'Oscuridad', 50, 10),
        Monstruo('Necromante', 'Oscuridad', 25, 20),
        Monstruo('Sombra Fugaz', 'Oscuridad', 20, 10),
        Monstruo('Vampiro Nocturno', 'Oscuridad', 40, 25),
        Monstruo('Vórtice Oscuro', 'Oscuridad', 35, 20),
        Monstruo('Centinela de la Oscuridad', 'Oscuridad', 30, 35),
        Monstruo('Aliento de la Muerte', 'Oscuridad', 45, 15),
        Monstruo('Guardián de las Tinieblas', 'Oscuridad', 35, 30),
        Monstruo('Serpiente de las Sombras', 'Oscuridad', 25, 20),
        Monstruo('Hechicero Oscuro', 'Oscuridad', 30, 15),
        Monstruo('Armadura de la Noche', 'Oscuridad', 20, 45),
        Monstruo('Anillo de Oscuridad', 'Oscuridad', 25, 25),
        Monstruo('Lobo Negro', 'Oscuridad', 40, 20),
        Monstruo('Escudo de las Sombras', 'Oscuridad', 15, 40),
        Monstruo('Espada de la Noche', 'Oscuridad', 35, 20),
    ]
    mazos_disponibles = {
    'Fuego': mazo_fuego,
    'Agua': mazo_agua,
    'Tierra': mazo_tierra,
    'Viento': mazo_viento,
    'Luz': mazo_luz,
    'Oscuridad': mazo_oscuridad
    }

    return mazos_disponibles

def mostrar_estado_juego(jugador1, jugador2):
    """
    Función para mostrar el estado actual del juego.
    """
    print("\n" + "="*40)
    print(f"Estado de {jugador1.nombre} (PV: {jugador1.puntos_vida})")
    print(f"Mano: {[c.nombre for c in jugador1.mano]}")
    print(f"Campo: {jugador1.campo}")
    
    print("\n" + "-"*40)
    
    print(f"Estado de {jugador2.nombre} (PV: {jugador2.puntos_vida})")
    print(f"Campo: {jugador2.campo}") # No mostramos la mano de la IA
    print("="*40 + "\n")

# --- Nueva clase para gestionar el flujo del juego ---
class Juego:
    """
    Clase principal que gestiona el flujo de la partida.
    """
    def __init__(self, jugador1, jugador2):
        self.jugador_actual = jugador1
        self.oponente = jugador2
        self.turno = 1
        
    def cambiar_turno(self):
        self.jugador_actual, self.oponente = self.oponente, self.jugador_actual
        self.turno += 1
        print(f"\n--- Comienza el Turno {self.turno}: {self.jugador_actual.nombre} ---")

    def fase_robo(self):
        print("Fase de Robo:")
        self.jugador_actual.robar_carta()

    def fase_invocacion(self):
        print("\nFase de Invocación:")
        # Implementación simple: si el jugador puede, invoca la primera carta de su mano
        if self.jugador_actual.mano and len(self.jugador_actual.campo) < 3:
            # Aquí podríamos pedir al jugador que elija una carta y posición.
            # Por ahora, una implementación simple:
            carta_a_invocar = self.jugador_actual.mano[0]
            posicion_elegida = 'ataque'
            self.jugador_actual.invocar_monstruo(0, posicion_elegida)
        else:
            print("No se pueden invocar monstruos en este momento.")

    def fase_batalla(self):
        print("\nFase de Batalla:")
        # Lógica de combate
        monstruos_atacantes = [m for m in self.jugador_actual.campo if m.posicion == 'ataque']
        
        if not monstruos_atacantes:
            print("No hay monstruos en posición de ataque para atacar.")
            return

        for monstruo_atacante in monstruos_atacantes:
            print(f"-> {monstruo_atacante.nombre} se prepara para atacar.")
            
            # Decidir el objetivo del ataque
            if not self.oponente.campo:
                # Ataque Directo
                print(f"  > ¡Ataque directo a {self.oponente.nombre}!")
                self.oponente.puntos_vida -= monstruo_atacante.ataque
                print(f"  > {monstruo_atacante.ataque} PV de daño. PV restantes: {self.oponente.puntos_vida}")
            else:
                # Ataque a Monstruo
                # Por ahora, simplemente ataca al primer monstruo en el campo del oponente
                monstruo_defensor = self.oponente.campo[0]
                
                print(f"  > ¡{monstruo_atacante.nombre} ataca a {monstruo_defensor.nombre}!")
                
                # Cálculo del daño (simplificado por ahora)
                diferencia_ataque = monstruo_atacante.ataque - monstruo_defensor.ataque
                
                if diferencia_ataque > 0:
                    print(f"  > {monstruo_atacante.nombre} destruye a {monstruo_defensor.nombre}.")
                    self.oponente.campo.remove(monstruo_defensor)
                    self.oponente.descartes.append(monstruo_defensor)
                    self.oponente.puntos_vida -= diferencia_ataque
                    print(f"  > Daño a PV de {self.oponente.nombre}: {diferencia_ataque}. PV restantes: {self.oponente.puntos_vida}")
                else:
                    print(f"  > Ambos monstruos se destruyen o no hay suficiente ataque.")
                    # Implementar la lógica completa de destrucción y daño
                    self.jugador_actual.campo.remove(monstruo_atacante)
                    self.jugador_actual.descartes.append(monstruo_atacante)
                    self.oponente.campo.remove(monstruo_defensor)
                    self.oponente.descartes.append(monstruo_defensor)
    
    def verificar_ganador(self):
        if self.jugador_actual.puntos_vida <= 0:
            print(f"\n¡{self.oponente.nombre} ha ganado el juego!")
            return True
        if self.oponente.puntos_vida <= 0:
            print(f"\n¡{self.jugador_actual.nombre} ha ganado el juego!")
            return True
        return False

# --- Lógica principal del juego ---
if __name__ == "__main__":
    
    # Preparamos a los jugadores
    print("--- Guardián de los Elementos ---")
    mazos = inicializar_mazos()
    
    # --- Jugador 1 ---
    nombre_jugador1 = input("Jugador 1, ¿cuál es tu nombre?: ")
    print("Mazos disponibles:", list(mazos.keys()))
    eleccion_mazo1 = input(f'{nombre_jugador1}, elige tu mazo (ej. Fuego): ')
    while eleccion_mazo1 not in mazos:
        eleccion_mazo1 = input("Ese mazo no existe. Elige uno de la lista: ")
    jugador1 = Jugador(nombre_jugador1, mazo=mazos[eleccion_mazo1])
    random.shuffle(jugador1.mazo)
    
    # --- Jugador 2 (IA simple) ---
    nombre_jugador2 = "IA"
    mazos_restantes = list(mazos.keys())
    mazos_restantes.remove(eleccion_mazo1)
    eleccion_mazo2 = random.choice(mazos_restantes)
    jugador2 = Jugador(nombre_jugador2, mazo=mazos[eleccion_mazo2])
    random.shuffle(jugador2.mazo)

    # Robo inicial de 3 cartas
    for _ in range(3):
        jugador1.robar_carta()
        jugador2.robar_carta()

    # Se inicia el objeto juego
    juego = Juego(jugador1, jugador2)
    
    # Bucle principal del juego
    while not juego.verificar_ganador():
        mostrar_estado_juego(juego.jugador_actual, juego.oponente)
        
        # Fases del turno
        juego.fase_robo()
        juego.fase_invocacion()
        juego.fase_batalla()

        # Cambiar el turno y repetir el bucle
        juego.cambiar_turno()
        input("Presiona Enter para continuar al siguiente turno...")