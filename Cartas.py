import random

def valor_carta(carta):
    if carta == 'J' or carta == 'Q' or carta == 'K':
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)

def ajustar_as(mano):
    while sum(mano) > 21 and 11 in mano:
        as_index = mano.index(11)
        mano[as_index] = 1

def obtener_carta_aleatoria():
    pintas = ["picas", "treboles", "diamantes", "corazones"]
    carta_valor = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
    return [valor_carta(carta_valor), carta_valor, random.choice(pintas)]

def pedir_carta_crupier(mano_crupier):
    
    while sum([carta[0] for carta in mano_crupier]) < 17:
        mano_crupier.append(obtener_carta_aleatoria())
        ajustar_as([carta[0] for carta in mano_crupier])

def mostrar_mano(mano):
    print(f"Mano: {[f'{carta[1]} de {carta[2]}' for carta in mano]}")

def mostrar_puntuacion(mano):
    print(f"Puntuación: {sum(carta[0] for carta in mano)}")

def mostrar_resultado(mano_jugador, mano_crupier):
    
    total_valor_jugador = sum([carta[0] for carta in mano_jugador])
    if total_valor_jugador > 21:
        print("¡Perdiste! Te pasaste de 21.")
    elif sum(mano_crupier) > 21 or total_valor_jugador > sum(mano_crupier):
        print("¡Ganaste!")
    elif total_valor_jugador == sum(mano_crupier):
        print("Empate.")
    else:
        print("¡Perdiste! La mano del crupier es mayor.")

def jugar_21():
    mano_jugador = [obtener_carta_aleatoria(), obtener_carta_aleatoria()]
    mano_crupier = [obtener_carta_aleatoria()]

    while sum([carta[0] for carta in mano_jugador]) < 21:
        mostrar_mano(mano_jugador)
        mostrar_puntuacion(mano_jugador)
        eleccion = input("¿Quieres tomar otra carta? (pedir/quedar): ").lower()

        if eleccion == 'pedir':
            mano_jugador.append(obtener_carta_aleatoria())
            ajustar_as([carta[0] for carta in mano_jugador])
        elif eleccion == 'quedar':
            break
        else:
            print("Opción no válida. Por favor, elige 'pedir' o 'quedar'.")

    pedir_carta_crupier(mano_crupier)

    mostrar_mano(mano_jugador)
    mostrar_puntuacion(mano_jugador)
    mostrar_mano(mano_crupier)
    mostrar_puntuacion(mano_crupier)

    mostrar_resultado(mano_jugador, mano_crupier)

while True:
    jugar_21()
    seguir_jugando = input("¿Quieres jugar otra partida? (sí/no): ").lower()
    if seguir_jugando != "sí":
        break
