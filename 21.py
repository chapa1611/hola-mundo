import random

def valor_carta(carta):
<<<<<<< HEAD
    if carta == 'J' or carta == 'Q' or carta == 'K':
=======
    if carta in ['J', 'Q', 'K']:
>>>>>>> 331b122f5b651b62c862d339de2e6f1ff4d48989
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)

def ajustar_as(mano):
<<<<<<< HEAD
    while sum(mano) > 21 and 11 in mano:
       as_index = mano.index(11)
       mano[as_index] = 1

def obtener_carta():
    pintas = ["picas", "treboles", "diamantes", "corazones"]
    carta_valor = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
    return [valor_carta(carta_valor), carta_valor, random.choice(pintas)]

def jugar_21():
    mano_jugador = [obtener_carta(), obtener_carta()]
    mano_crupier = [obtener_carta()]

    while sum([carta[0] for carta in mano_jugador]) < 21:
        print(f"Tu mano: {[f'{carta[1]} de {carta[2]}' for carta in mano_jugador]}")
        eleccion = input("¿Quieres tomar otra carta? (pedir/quedar): ").lower()

        if eleccion == 'pedir':
            mano_jugador.append(obtener_carta())
            ajustar_as([carta[0] for carta in mano_jugador])
        else:
            break

    while sum([carta[0] for carta in mano_crupier]) < 17:
        mano_crupier.append(obtener_carta())
        ajustar_as([carta[0] for carta in mano_crupier])

    print(f"\nTu mano final: {[f'{carta[1]} de {carta[2]}' for carta in mano_jugador]}")
    print(f"Mano del crupier: {[f'{carta[1]} de {carta[2]}' for carta in mano_crupier]}")

    if sum([carta[0] for carta in mano_jugador]) > 21:
        print("¡Perdiste! Te pasaste de 21.")
    elif sum([carta[0] for carta in mano_crupier]) > 21 or sum([carta[0] for carta in mano_jugador]) > sum([carta[0] for carta in mano_crupier]):
        print("¡Ganaste!")
    elif sum([carta[0] for carta in mano_jugador]) == sum([carta[0] for carta in mano_crupier]):
=======
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
>>>>>>> 331b122f5b651b62c862d339de2e6f1ff4d48989
        print("Empate.")
    else:
        print("¡Perdiste! La mano del crupier es mayor.")

<<<<<<< HEAD
jugar_21()
=======
jugar_21()

>>>>>>> 331b122f5b651b62c862d339de2e6f1ff4d48989
