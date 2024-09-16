vides = int(input("Quantes vides tens?"))
print(vides)
while vides >0:
    tecla = input("Presiona 'k' per perdre una vida: ")
    if tecla == 'k':
            vides -= 1
            print("Vides restants:", vides)
    if vides == 0:
        print("GAME OVER")
    if vides == 0:
        break
