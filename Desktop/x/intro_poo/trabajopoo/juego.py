from random import shuffle

class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def dar_valor(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        if self.valor == 'A':
            return 11
        return int(self.valor)

    def mostrar(self):
        return f"{self.valor} de {self.pinta}"

class Mazo:
    def __init__(self, jugador=False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [Carta(v, p)
                           for v in ['A', 'J', 'Q', 'K'] + [str(x) for x in range(2, 11)]
                           for p in ['picas', 'treboles', 'corazones', 'diamantes']]
        shuffle(self.cartas)

    def dar_valor(self):
        valor = 0
        for c in self.cartas:
            valor += c.dar_valor()
        return valor

    def tiene_as(self):
        for c in self.cartas:
            if c.valor == "A":
                return True
        return False

    def dar_carta(self):
        return self.cartas.pop()

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def mostrar_carta(self, todas=False):
        if todas:
            print(self.cartas[0].mostrar())
        else:
            print("* de *")
        for c in self.cartas[1:]:
            print(c.mostrar())

class Jugador:
    def __init__(self):
        self.mano = []

    def agregar_carta(self, carta):
        self.mano.append(carta)

    def obtener_puntuacion(self):
        return sum(carta.dar_valor() for carta in self.mano)

    def ajustar_as(self):
        for carta in self.mano:
            if carta.valor == 'A' and self.obtener_puntuacion() > 21:
                carta.valor = 1

    def mostrar_mano(self):
        return [carta.mostrar() for carta in self.mano]

    def mostrar_puntuacion(self):
        print(f"Puntuación actual: {self.obtener_puntuacion()}")

class Casa(Jugador):
    def mostrar_mano(self, todas=False):
        if todas or (len(self.mano) == 1 and self.mano[0].mostrar() == "* de *"):
            return super().mostrar_mano()
        else:
            return super().mostrar_mano()[:-1] + [carta.mostrar() for carta in self.mano[-1:]]

class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.casa = Casa()
        self.jugador = Jugador()
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0
        self.empates = 0

    def iniciar_juego(self):
        self.casa = Casa()
        self.jugador = Jugador()
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())

    def pedir_carta(self):
        carta_jugador = self.mazo.dar_carta()
        self.jugador.agregar_carta(carta_jugador)
        self.jugador.ajustar_as()

    def jugar_ronda(self):
        if self.jugador.obtener_puntuacion() == 21 and len(self.jugador.mano) == 2:
            self.mostrar_juego()
            print("¡Ganaste con Blackjack!")
            return

        while True:
            self.mostrar_juego()
            self.jugador.mostrar_puntuacion()

            if self.jugador.obtener_puntuacion() > 21:
                print("¡Perdiste! Te pasaste de 21.")
                self.partidas_perdidas += 1
                break

            eleccion = input("¿Quieres tomar otra carta? (pedir/quedar): ").lower()

            if eleccion == 'pedir':
                self.pedir_carta()
            elif eleccion == 'quedar':
                break
            else:
                print("Opción no válida. Por favor, elige 'pedir' o 'quedar'.")

        while self.casa.obtener_puntuacion() < 17:
            carta_casa = self.mazo.dar_carta()
            self.casa.agregar_carta(carta_casa)
            self.casa.ajustar_as()

        self.mostrar_juego()
        self.mostrar_resultado()

    def mostrar_juego(self):
        print("Jugador:")
        print(self.jugador.mostrar_mano())
        print("Casa:")
        print(self.casa.mostrar_mano())

    def mostrar_resultado(self):
        punt_jugador = self.jugador.obtener_puntuacion()
        punt_casa = self.casa.obtener_puntuacion()

        if punt_jugador > 21:
            print("¡Perdiste! Te pasaste de 21.")
            self.partidas_perdidas += 1
        elif punt_casa > 21 or punt_jugador > punt_casa:
            print("¡Ganaste!")
            self.partidas_ganadas += 1
        elif punt_jugador == punt_casa:
            print("Empate.")
            self.empates += 1
        else:
            print("¡Perdiste! La mano de la casa es mayor.")
            self.partidas_perdidas += 1

    def mostrar_puntaje(self):
        print(f"\nPartidas ganadas: {self.partidas_ganadas}")
        print(f"Partidas perdidas: {self.partidas_perdidas}")
        print(f"Empates: {self.empates}")

