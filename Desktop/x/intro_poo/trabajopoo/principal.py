from juego import *

if __name__ == "__main__":
    juego = Juego()

    while True:
        juego.iniciar_juego()
        juego.jugar_ronda()
        juego.mostrar_puntaje()

        seguir_jugando = input("¿Quieres jugar otra partida? (sí/no): ").lower()
        if seguir_jugando != "sí" and seguir_jugando != "si":
            break