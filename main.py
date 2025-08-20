import tkinter as tk
from cartas import Monstruo, Jugador
import random

def inicializar_mazos():
    """
    Función para crear y devolver una lista de todos los mazos.
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

# --- Clase Juego Mejorada con Interacción ---
class Juego:
    """
    Clase principal que gestiona el flujo de la partida.
    """
    def __init__(self, jugador1, jugador2):
        self.jugador_actual = jugador1
        self.oponente = jugador2
        self.turno = 1
        self.tabla_afinidades = {
            'Tierra': {'ventaja': 'Agua', 'desventaja': 'Fuego'},
            'Agua': {'ventaja': 'Fuego', 'desventaja': 'Aire'},
            'Fuego': {'ventaja': 'Aire', 'desventaja': 'Tierra'},
            'Aire': {'ventaja': 'Oscuridad', 'desventaja': 'Luz'},
            'Luz': {'ventaja': 'Tierra', 'desventaja': 'Oscuridad'},
            'Oscuridad': {'ventaja': 'Luz', 'desventaja': 'Agua'},
        }

    def cambiar_turno(self):
        self.jugador_actual, self.oponente = self.oponente, self.jugador_actual
        self.turno += 1
        print(f"\n--- Comienza el Turno {self.turno}: {self.jugador_actual.nombre} ---")

    def fase_robo(self):
        print("Fase de Robo:")
        self.jugador_actual.robar_carta()

    def fase_invocacion(self):
        print("\nFase de Invocación:")
        if self.jugador_actual.nombre != "IA" and self.jugador_actual.mano:
            print("Cartas en tu mano:")
            for i, carta in enumerate(self.jugador_actual.mano):
                print(f"  [{i}] {carta.nombre} (ATK:{carta.ataque} DEF:{carta.defensa})")
            
            eleccion_str = input("Elige el número de la carta que quieres invocar (o 'no' para no invocar): ")
            if eleccion_str.lower() == 'no':
                print("No has invocado un monstruo.")
                return

            try:
                indice_carta = int(eleccion_str)
                posicion_elegida = input("Elige la posición ('ataque' o 'defensa'): ").lower()
                
                if posicion_elegida not in ['ataque', 'defensa']:
                    print("Posición no válida. Por favor, elige 'ataque' o 'defensa'.")
                    return
                
                self.jugador_actual.invocar_monstruo(indice_carta, posicion_elegida)

            except (ValueError, IndexError):
                print("Entrada no válida. No se invocó ningún monstruo.")
        
        elif len(self.jugador_actual.campo) < 3:
            # Lógica de IA simple
            if self.jugador_actual.mano:
                carta_a_invocar = self.jugador_actual.mano[0]
                posicion_elegida = random.choice(['ataque', 'defensa'])
                self.jugador_actual.invocar_monstruo(0, posicion_elegida)

    def fase_batalla(self):
        print("\nFase de Batalla:")
        monstruos_atacantes = [m for m in self.jugador_actual.campo if m.posicion == 'ataque']
        
        if not monstruos_atacantes:
            print("No hay monstruos en posición de ataque para atacar.")
            return

        if self.jugador_actual.nombre != "IA":
            if not self.oponente.campo:
                confirmacion = input("¿Quieres realizar un ataque directo? (si/no): ")
                if confirmacion.lower() == 'si':
                    for monstruo_atacante in monstruos_atacantes:
                        self.resolver_ataque(monstruo_atacante, None)
            else:
                for monstruo_atacante in monstruos_atacantes:
                    print(f"-> {monstruo_atacante.nombre} (ATK:{monstruo_atacante.ataque}) puede atacar.")
                    
                    opciones_oponente = [m for m in self.oponente.campo]
                    print("Monstruos en el campo del oponente:")
                    for i, m in enumerate(opciones_oponente):
                        print(f"  [{i}] {m.nombre} (POSICIÓN:{m.posicion} - ATK:{m.ataque} DEF:{m.defensa})")
                    
                    eleccion_str = input("Elige el número del monstruo a atacar (o 'no' para no atacar con este monstruo): ")
                    if eleccion_str.lower() != 'no':
                        try:
                            indice_defensor = int(eleccion_str)
                            if 0 <= indice_defensor < len(opciones_oponente):
                                monstruo_defensor = opciones_oponente[indice_defensor]
                                self.resolver_ataque(monstruo_atacante, monstruo_defensor)
                            else:
                                print("Opción no válida.")
                        except ValueError:
                            print("Entrada no válida.")
        else: # Lógica para la IA
            for monstruo_atacante in monstruos_atacantes:
                if self.oponente.campo:
                    monstruo_defensor = self.oponente.campo[0]
                    self.resolver_ataque(monstruo_atacante, monstruo_defensor)
                else:
                    self.resolver_ataque(monstruo_atacante, None)

    def resolver_ataque(self, atacante, defensor):
        """Función auxiliar para la lógica de combate."""
        print(f"-> {atacante.nombre} se prepara para atacar.")
        
        if defensor is None:
            # Ataque Directo
            print(f"  > ¡Ataque directo a {self.oponente.nombre}!")
            self.oponente.puntos_vida -= atacante.ataque
            print(f"  > {atacante.ataque} PV de daño. PV restantes: {self.oponente.puntos_vida}")
            return

        print(f"  > ¡{atacante.nombre} ataca a {defensor.nombre}!")
        
        dano_duplicado = 1
        if self.tabla_afinidades[atacante.tipo]['ventaja'] == defensor.tipo:
            dano_duplicado = 2
            print(f"  > ¡Ataque efectivo! {atacante.tipo} tiene ventaja sobre {defensor.tipo}.")

        if defensor.posicion == 'ataque':
            dano_final = (atacante.ataque - defensor.ataque) * dano_duplicado
            
            if dano_final > 0:
                print(f"  > {atacante.nombre} destruye a {defensor.nombre}.")
                self.oponente.campo.remove(defensor)
                self.oponente.descartes.append(defensor)
                self.oponente.puntos_vida -= dano_final
                print(f"  > Daño a PV de {self.oponente.nombre}: {dano_final}. PV restantes: {self.oponente.puntos_vida}")
            elif dano_final < 0:
                dano_propio = abs(dano_final)
                print(f"  > {defensor.nombre} destruye a {atacante.nombre}.")
                self.jugador_actual.campo.remove(atacante)
                self.jugador_actual.descartes.append(atacante)
                self.jugador_actual.puntos_vida -= dano_propio
                print(f"  > Daño a PV de {self.jugador_actual.nombre}: {dano_propio}. PV restantes: {self.jugador_actual.puntos_vida}")
            else:
                print("  > Ambos monstruos tienen el mismo ataque. Se destruyen mutuamente.")
                self.jugador_actual.campo.remove(atacante)
                self.jugador_actual.descartes.append(atacante)
                self.oponente.campo.remove(defensor)
                self.oponente.descartes.append(defensor)

        elif defensor.posicion == 'defensa':
            dano_defensa = (atacante.ataque - defensor.defensa) * dano_duplicado

            if dano_defensa > 0:
                print(f"  > {atacante.nombre} ataca al monstruo en defensa y lo destruye.")
                self.oponente.campo.remove(defensor)
                self.oponente.descartes.append(defensor)
                print("  > No hay daño a los puntos de vida del oponente.")
            elif dano_defensa < 0:
                print(f"  > El ataque no es suficiente. {defensor.nombre} resiste el ataque.")
                dano_propio_defensa = abs(dano_defensa)
                self.jugador_actual.puntos_vida -= dano_propio_defensa
                print(f"  > {defensor.nombre} causó daño de rebote. Daño a PV de {self.jugador_actual.nombre}: {dano_propio_defensa}. PV restantes: {self.jugador_actual.puntos_vida}")
            else:
                print("  > El ataque es igual a la defensa. El monstruo resiste pero no hay daño de rebote.")

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

# --- Interfaz Gráfica (GUI) ---
class App(tk.Tk):
    def __init__(self, juego):
        super().__init__()
        self.juego = juego
        self.title("Guardián de los Elementos")
        self.geometry("800x600")

        # Configuración de la interfaz
        self.crear_widgets()
        self.actualizar_ui()
    
    def crear_widgets(self):
        # Frame principal para contener todo
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame del jugador 2 (oponente)
        oponente_frame = tk.LabelFrame(main_frame, text="Oponente (IA)", padx=10, pady=10)
        oponente_frame.pack(pady=10)
        self.pv_oponente_label = tk.Label(oponente_frame, text=f"PV: {self.juego.oponente.puntos_vida}")
        self.pv_oponente_label.pack()
        
        self.campo_oponente_label = tk.Label(oponente_frame, text="Campo: [Monstruos del oponente]")
        self.campo_oponente_label.pack()
        
        # Frame del jugador 1 (humano)
        jugador_frame = tk.LabelFrame(main_frame, text=self.juego.jugador_actual.nombre, padx=10, pady=10)
        jugador_frame.pack(pady=20)
        self.pv_jugador_label = tk.Label(jugador_frame, text=f"PV: {self.juego.jugador_actual.puntos_vida}")
        self.pv_jugador_label.pack()
        
        self.campo_jugador_label = tk.Label(jugador_frame, text="Campo: [Monstruos del jugador]")
        self.campo_jugador_label.pack()
        
        # Botón para simular el turno (reemplazará el input de la consola)
        self.boton_turno = tk.Button(self, text="Pasar Turno", command=self.siguiente_turno)
        self.boton_turno.pack(pady=10)
        
        # Consola para mensajes del juego
        self.consola_texto = tk.Text(self, height=10, width=70)
        self.consola_texto.pack(pady=10)
        self.consola_texto.insert(tk.END, "¡Bienvenido a Guardián de los Elementos!")

    def actualizar_ui(self):
        # Esta función se encargará de refrescar todos los datos en la GUI
        self.pv_jugador_label.config(text=f"PV: {self.juego.jugador_actual.puntos_vida}")
        self.pv_oponente_label.config(text=f"PV: {self.juego.oponente.puntos_vida}")
        
        # Aquí iría la lógica para mostrar las cartas en mano y campo
        campo_jugador_nombres = [m.nombre for m in self.juego.jugador_actual.campo]
        self.campo_jugador_label.config(text=f"Campo: {campo_jugador_nombres}")
        
        campo_oponente_nombres = [m.nombre for m in self.juego.oponente.campo]
        self.campo_oponente_label.config(text=f"Campo: {campo_oponente_nombres}")
    
    def log(self, mensaje):
        self.consola_texto.insert(tk.END, "\n" + mensaje)
        self.consola_texto.see(tk.END) # Auto-scroll

    def siguiente_turno(self):
        # Simula un turno completo y actualiza la GUI
        self.juego.fase_robo()
        self.juego.fase_invocacion()
        self.juego.fase_batalla()
        self.juego.cambiar_turno()
        self.actualizar_ui()
        self.log(f"Turno de {self.juego.jugador_actual.nombre}")

# --- Bucle principal ---
if __name__ == "__main__":
    
    # Preparamos a los jugadores
    mazos = inicializar_mazos()
    jugador1 = Jugador("Tu", mazo=mazos['Fuego']) # Simplificado para el ejemplo
    jugador2 = Jugador("IA", mazo=mazos['Agua'])  # Simplificado para el ejemplo
    random.shuffle(jugador1.mazo)
    random.shuffle(jugador2.mazo)
    for _ in range(3):
        jugador1.robar_carta()
        jugador2.robar_carta()

    juego = Juego(jugador1, jugador2)
    
    # Inicia la aplicación de Tkinter
    app = App(juego)
    app.mainloop()