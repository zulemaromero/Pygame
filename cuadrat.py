vidas = int(input("Quantes vides tens? "))
ample_caixa = 20
alt_caixa = 10
posicio_asterisc_x = 0
posicio_asterisc_y = 0

while True:
    print("-" * (ample_caixa + 2))

    for i in range(alt_caixa):
        print('|', end='')
        for j in range(ample_caixa):
            if i == posicio_asterisc_y and j == posicio_asterisc_x:
                print('*', end='')
            else:
                print(' ', end='')
        print('|')

    print("-" * (ample_caixa + 2))

    tecla = input("Clica 'a' per moure a l'esquerra, 'd' per moure a la dreta, 'w' per moure cap amunt, 's' per moure cap avall i 'k' per perdre una vida: ")

    if tecla == 'a' and posicio_asterisc_x > 0:
        posicio_asterisc_x -= 1
    elif tecla == 'd' and posicio_asterisc_x < ample_caixa - 1:
        posicio_asterisc_x += 1
    elif tecla == 'w' and posicio_asterisc_y > 0:
        posicio_asterisc_y -= 1
    elif tecla == 's' and posicio_asterisc_y < alt_caixa - 1:
        posicio_asterisc_y += 1
    if tecla == 'k':
        vidas -= 1
        print("Has perdut una vids")
    if vidas == 0:
        print('Game Over!')
        break
