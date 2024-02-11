import random

def valor_carta(carta):
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
    mano_jugador = [valor_carta(random.choice(cartas)), valor_carta(random.choice(cartas))]
    mano_crupier = [valor_carta(random.choice(cartas))]

    while sum(mano_jugador) < 21:
        print(f"Tu mano: {mano_jugador}")
        eleccion = input("¿Quieres tomar otra carta? (pedir/quedar): ").lower()

        if eleccion == 'pedir':
            mano_jugador.append(valor_carta(random.choice(cartas)))
            ajustar_as(mano_jugador)
        else:
            break

    while sum(mano_crupier) < 17:
        mano_crupier.append(valor_carta(random.choice(cartas)))
        ajustar_as(mano_crupier)

    print(f"\nTu mano final: {mano_jugador}")
    print(f"Mano del crupier: {mano_crupier}")

    if sum(mano_jugador) > 21:
        print("¡Perdiste! Te pasaste de 21.")
    elif sum(mano_crupier) > 21 or sum(mano_jugador) > sum(mano_crupier):
        print("¡Ganaste!")
    elif sum(mano_jugador) == sum(mano_crupier):
        print("Empate.")
    else:
        print("¡Perdiste! La mano del crupier es mayor.")

jugar_21()

