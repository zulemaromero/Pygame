input("""Per anar a l'esquerra presiona "a"
Per anar a la dreta presiona "d" : """)
posicio = 0
amplada = 21
while True:

    moviment_pantalla = input(":")

    if moviment_pantalla == "a":
        posicio = posicio - 1
        if posicio <= -1:
            posicio += 1
    if moviment_pantalla == "d":
        posicio = posicio + 1
        if posicio >= 21:
            posicio -= 1
    if moviment_pantalla == "w":
        print("Tecla erronea")
    if moviment_pantalla == "s":
        print("Tecla erronea")

    text = "|"
    for i in range(amplada):
        if i == posicio:
            text+="*"
        else:
            text += "."
    text += "|"
    print(text)
    print(posicio)
