import tkinter as tk
import random
from cartas import Monstruo, Jugador

def inicializar_mazos():
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

class Juego:
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

    def fase_robo(self):
        self.jugador_actual.robar_carta()

    def fase_invocacion(self, indice_carta=None, posicion_elegida=None):
        if self.jugador_actual.nombre != "IA":
            if indice_carta is not None and posicion_elegida:
                self.jugador_actual.invocar_monstruo(indice_carta, posicion_elegida)
        elif len(self.jugador_actual.campo) < 3:
            if self.jugador_actual.mano:
                carta_a_invocar = self.jugador_actual.mano[0]
                posicion_elegida = random.choice(['ataque', 'defensa'])
                self.jugador_actual.invocar_monstruo(0, posicion_elegida)
    
    def fase_batalla(self, atacante=None, defensor=None):
        if self.jugador_actual.nombre == "IA":
            monstruos_atacantes = [m for m in self.jugador_actual.campo if m.posicion == 'ataque' and not m.has_attacked]
            for monstruo_atacante in monstruos_atacantes:
                if self.oponente.campo:
                    monstruo_defensor = self.oponente.campo[0]
                    self.resolver_ataque(monstruo_atacante, monstruo_defensor)
                else:
                    self.resolver_ataque(monstruo_atacante, None)
                monstruo_atacante.has_attacked = True
        else:
            if atacante is not None:
                self.resolver_ataque(atacante, defensor)
                atacante.has_attacked = True

    def resolver_ataque(self, atacante, defensor):
        app.log(f"-> {atacante.nombre} (ATK: {atacante.ataque} DEF: {atacante.defensa}) se prepara para atacar.")
        
        if defensor is None:
            app.log(f"  > ¡Ataque directo a {self.oponente.nombre}!")
            self.oponente.puntos_vida -= atacante.ataque
            app.log(f"  > {atacante.ataque} PV de daño. PV restantes: {self.oponente.puntos_vida}")
            return

        app.log(f"  > ¡{atacante.nombre} ataca a {defensor.nombre}!")
        
        dano_duplicado = 1
        if self.tabla_afinidades[atacante.tipo]['ventaja'] == defensor.tipo:
            dano_duplicado = 2
            app.log(f"  > ¡Ataque efectivo! {atacante.tipo} tiene ventaja sobre {defensor.tipo}.")

        if defensor.posicion == 'ataque':
            dano_final = (atacante.ataque - defensor.ataque) * dano_duplicado
            
            if dano_final > 0:
                app.log(f"  > {atacante.nombre} destruye a {defensor.nombre}.")
                self.oponente.campo.remove(defensor)
                self.oponente.descartes.append(defensor)
                self.oponente.puntos_vida -= dano_final
                app.log(f"  > Daño a PV de {self.oponente.nombre}: {dano_final}. PV restantes: {self.oponente.puntos_vida}")
            elif dano_final < 0:
                dano_propio = abs(dano_final)
                app.log(f"  > {defensor.nombre} destruye a {atacante.nombre}.")
                self.jugador_actual.campo.remove(atacante)
                self.jugador_actual.descartes.append(atacante)
                self.jugador_actual.puntos_vida -= dano_propio
                app.log(f"  > Daño a PV de {self.jugador_actual.nombre}: {dano_propio}. PV restantes: {self.jugador_actual.puntos_vida}")
            else:
                app.log("  > Ambos monstruos tienen el mismo ataque. Se destruyen mutuamente.")
                self.jugador_actual.campo.remove(atacante)
                self.jugador_actual.descartes.append(atacante)
                self.oponente.campo.remove(defensor)
                self.oponente.descartes.append(defensor)

        elif defensor.posicion == 'defensa':
            dano_defensa = (atacante.ataque - defensor.defensa) * dano_duplicado

            if dano_defensa > 0:
                app.log(f"  > {atacante.nombre} ataca al monstruo en defensa y lo destruye.")
                self.oponente.campo.remove(defensor)
                self.oponente.descartes.append(defensor)
                app.log("  > No hay daño a los puntos de vida del oponente.")
            elif dano_defensa < 0:
                app.log(f"  > El ataque no es suficiente. {defensor.nombre} resiste el ataque.")
                dano_propio_defensa = abs(dano_defensa)
                self.jugador_actual.puntos_vida -= dano_propio_defensa
                app.log(f"  > {defensor.nombre} causó daño de rebote. Daño a PV de {self.jugador_actual.nombre}: {dano_propio_defensa}. PV restantes: {self.jugador_actual.puntos_vida}")
            else:
                app.log("  > El ataque es igual a la defensa. El monstruo resiste pero no hay daño de rebote.")

    def verificar_ganador(self):
        if self.jugador_actual.puntos_vida <= 0:
            app.log(f"\n¡{self.oponente.nombre} ha ganado el juego!")
            app.show_game_over_screen()
            return True
        if self.oponente.puntos_vida <= 0:
            app.log(f"\n¡{self.jugador_actual.nombre} ha ganado el juego!")
            app.show_game_over_screen()
            return True
        return False
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guardián de los Elementos")
        self.geometry("800x600")
        self.all_widgets = []
        self.show_main_menu()

    def clear_screen(self):
        for widget in self.all_widgets:
            widget.destroy()
        self.all_widgets.clear()
        
    def show_main_menu(self):
        self.clear_screen()
        
        main_menu_frame = tk.Frame(self)
        main_menu_frame.pack(expand=True)
        self.all_widgets.append(main_menu_frame)

        label_title = tk.Label(main_menu_frame, text="Guardián de los Elementos", font=("Arial", 24))
        label_title.pack(pady=20)
        
        label_prompt = tk.Label(main_menu_frame, text="Selecciona tu mazo:", font=("Arial", 16))
        label_prompt.pack(pady=10)
        
        mazos = inicializar_mazos()
        for mazo_nombre in mazos.keys():
            btn_mazo = tk.Button(main_menu_frame, text=mazo_nombre, command=lambda mazo=mazo_nombre: self.start_game(mazo))
            btn_mazo.pack(pady=5)
            
    def start_game(self, mazo_elegido):
        self.clear_screen()
        
        mazos = inicializar_mazos()
        
        jugador1 = Jugador("Jugador", mazo=mazos[mazo_elegido])
        mazos_restantes = list(mazos.keys())
        mazos_restantes.remove(mazo_elegido)
        ia_mazo = random.choice(mazos_restantes)
        jugador2 = Jugador("IA", mazo=mazos[ia_mazo])
        
        random.shuffle(jugador1.mazo)
        random.shuffle(jugador2.mazo)
        
        for _ in range(3):
            jugador1.robar_carta()
            jugador2.robar_carta()
            
        self.juego = Juego(jugador1, jugador2)
        
        self.fase = 'invocacion'
        self.monstruo_invocando = None
        
        self.pv_jugador_var = tk.StringVar(self, value=f"PV: {self.juego.jugador_actual.puntos_vida}")
        self.pv_oponente_var = tk.StringVar(self, value=f"PV: {self.juego.oponente.puntos_vida}")
        
        self.crear_widgets()
        self.actualizar_interfaz()

        self.log("¡El juego ha comenzado!")
        self.log(f"Tu mazo es: {mazo_elegido}")
        self.log(f"El mazo de la IA es: {ia_mazo}")
        self.log(f"Turno 1: {self.juego.jugador_actual.nombre}")
        self.log("No puedes atacar en el primer turno. Solo puedes invocar un monstruo.")
        
    def crear_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.all_widgets.append(main_frame)

        oponente_frame = tk.LabelFrame(main_frame, text="Oponente (IA)", padx=10, pady=10)
        oponente_frame.pack(fill=tk.X, pady=5)
        self.all_widgets.append(oponente_frame)
        self.pv_oponente_label = tk.Label(oponente_frame, textvariable=self.pv_oponente_var)
        self.pv_oponente_label.pack()
        self.marco_campo_oponente = tk.Frame(oponente_frame)
        self.marco_campo_oponente.pack()

        self.consola_texto = tk.Text(main_frame, height=10, width=70)
        self.consola_texto.pack(pady=10)
        self.all_widgets.append(self.consola_texto)

        self.btn_pasar_turno = tk.Button(main_frame, text="Pasar Turno", command=self.pasar_turno)
        self.btn_pasar_turno.pack(pady=5)
        self.all_widgets.append(self.btn_pasar_turno)
        
        jugador_frame = tk.LabelFrame(main_frame, text=self.juego.jugador_actual.nombre, padx=10, pady=10)
        jugador_frame.pack(fill=tk.X, pady=5)
        self.all_widgets.append(jugador_frame)
        self.pv_jugador_label = tk.Label(jugador_frame, textvariable=self.pv_jugador_var)
        self.pv_jugador_label.pack()
        self.marco_campo_jugador = tk.Frame(jugador_frame)
        self.marco_campo_jugador.pack()
        self.marco_mano = tk.LabelFrame(jugador_frame, text="Mano")
        self.marco_mano.pack(pady=5)

    def log(self, mensaje):
        self.consola_texto.insert(tk.END, "\n" + mensaje)
        self.consola_texto.see(tk.END)

    def actualizar_interfaz(self):
        self.pv_jugador_var.set(f"PV: {self.juego.jugador_actual.puntos_vida}")
        self.pv_oponente_var.set(f"PV: {self.juego.oponente.puntos_vida}")

        for widget in self.marco_mano.winfo_children():
            widget.destroy()
        if self.fase == 'invocacion':
            for i, carta in enumerate(self.juego.jugador_actual.mano):
                btn = tk.Button(self.marco_mano, text=f"{carta.nombre} (ATK: {carta.ataque} DEF: {carta.defensa})", command=lambda idx=i: self.elegir_posicion(idx))
                btn.pack(side=tk.LEFT, padx=5)
        elif self.fase == 'elegir_posicion':
            btn_ataque = tk.Button(self.marco_mano, text="Invocar en Ataque", command=lambda: self.invocar_carta_final('ataque'))
            btn_ataque.pack(side=tk.LEFT, padx=5)
            btn_defensa = tk.Button(self.marco_mano, text="Invocar en Defensa", command=lambda: self.invocar_carta_final('defensa'))
            btn_defensa.pack(side=tk.LEFT, padx=5)
        else: # Fase de batalla o final de invocación
             pass

        for widget in self.marco_campo_jugador.winfo_children():
            widget.destroy()
        for monstruo in self.juego.jugador_actual.campo:
            btn = tk.Button(self.marco_campo_jugador, text=f"{monstruo.nombre} ({monstruo.posicion})", command=lambda m=monstruo: self.seleccionar_atacante(m))
            if self.juego.turno > 1 and monstruo.posicion == 'ataque' and not monstruo.has_attacked:
                btn.config(state=tk.NORMAL)
            else:
                btn.config(state=tk.DISABLED)
            btn.pack(side=tk.LEFT, padx=5)

        for widget in self.marco_campo_oponente.winfo_children():
            widget.destroy()
        for monstruo in self.juego.oponente.campo:
            lbl = tk.Label(self.marco_campo_oponente, text=f"{monstruo.nombre} ({monstruo.posicion})")
            lbl.pack(side=tk.LEFT, padx=5)
    
    def elegir_posicion(self, indice):
        self.monstruo_invocando = indice
        self.fase = 'elegir_posicion'
        self.actualizar_interfaz()

    def invocar_carta_final(self, posicion):
        if self.juego.jugador_actual.invocar_monstruo(self.monstruo_invocando, posicion):
            self.log(f"Has invocado a {self.juego.jugador_actual.campo[-1].nombre} en posición de {posicion}.")
            if self.juego.turno > 1:
                self.fase = 'batalla'
                self.log("Fase de Batalla. Selecciona un monstruo en tu campo para atacar.")
            else:
                self.fase = 'final_invocacion'
                self.log("Primer turno. No puedes atacar. Por favor, pasa el turno.")
            self.monstruo_invocando = None
        else:
            self.log("No se pudo invocar al monstruo.")
        self.actualizar_interfaz()
        
    def seleccionar_atacante(self, monstruo_atacante):
        if self.juego.turno > 1 and monstruo_atacante.posicion == 'ataque' and not monstruo_atacante.has_attacked:
            if not self.juego.oponente.campo:
                self.juego.fase_batalla(atacante=monstruo_atacante, defensor=None)
            else:
                defensor = self.juego.oponente.campo[0]
                self.juego.fase_batalla(atacante=monstruo_atacante, defensor=defensor)
            
            self.actualizar_interfaz()
            if self.juego.verificar_ganador():
                self.log("¡El juego ha terminado!")
        elif self.juego.turno == 1:
            self.log("No puedes atacar en el primer turno.")
        
    def pasar_turno(self):
        for monstruo in self.juego.jugador_actual.campo:
            monstruo.has_attacked = False

        self.log(f"--- Turno de la IA: {self.juego.oponente.nombre} ---")
        self.juego.cambiar_turno()
        self.juego.fase_robo()
        self.juego.fase_invocacion()

        if self.juego.turno > 2:
            self.juego.fase_batalla()
        else:
            self.log("La IA no puede atacar en su primer turno.")

        for monstruo in self.juego.oponente.campo:
            monstruo.has_attacked = False

        self.juego.cambiar_turno()
        self.log(f"\n--- Comienza el Turno {self.juego.turno}: {self.juego.jugador_actual.nombre} ---")
        self.fase = 'invocacion'
        self.log("Fase de Robo del Jugador.")
        self.juego.fase_robo()
        self.actualizar_interfaz()
        
        if self.juego.verificar_ganador():
            self.log("¡El juego ha terminado!")
            
    def show_game_over_screen(self):
        self.btn_pasar_turno.config(state=tk.DISABLED)
        
        game_over_frame = tk.LabelFrame(self, text="Fin del juego", padx=10, pady=10)
        game_over_frame.pack(pady=20)
        self.all_widgets.append(game_over_frame)
        
        btn_reiniciar = tk.Button(game_over_frame, text="Jugar de Nuevo", command=self.show_main_menu)
        btn_reiniciar.pack(side=tk.LEFT, padx=10)
        
        btn_salir = tk.Button(game_over_frame, text="Salir", command=self.destroy)
        btn_salir.pack(side=tk.RIGHT, padx=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()