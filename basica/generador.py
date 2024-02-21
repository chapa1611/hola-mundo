pintas = ["picas", "treboles", "diamantes", "corazones"]
valores = ["A", "J", "Q", "K"] + [str(i) for i in range(2, 11)]
mazo = [(v, p) for v in valores for p in pintas]
for c in mazo:
    print(c)