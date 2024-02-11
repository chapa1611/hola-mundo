import random
import time

def asignar_valor_carta(carta):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)

def ajustar_as(mano):
    if sum(mano) > 21 and 11 in mano:
        mano.remove(11)
        mano.append(1)

def jugar_21():
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    mano_jugador = [asignar_valor_carta(random.choice(cartas)) for _ in range(2)]
    mano_crupier = [asignar_valor_carta(random.choice(cartas)) for _ in range(2)]

    print(f"Tu mano inicial: {mano_jugador}")

    while sum(mano_jugador) < 21:
        eleccion = input("¿Quieres tomar otra carta? (s/n): ").lower()

        if eleccion == 's':
            mano_jugador.append(asignar_valor_carta(random.choice(cartas)))
            ajustar_as(mano_jugador)
            print(f"Tu mano: {mano_jugador}")
            time.sleep(1)  # Pausa de 1 segundo
        else:
            break

    print(f"Tu mano final: {mano_jugador}")
    print(f"Mano del crupier: {mano_crupier}")

    while sum(mano_crupier) < 17:
        mano_crupier.append(asignar_valor_carta(random.choice(cartas)))
        ajustar_as(mano_crupier)
        print(f"Mano del crupier: {mano_crupier}")
        time.sleep(1)  # Pausa de 1 segundo

    print(f"Mano final del crupier: {mano_crupier}")

if __name__ == "__main__":
    jugar_21()
