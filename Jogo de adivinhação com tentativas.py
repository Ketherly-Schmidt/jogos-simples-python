import random

print('='*50)
print(' '*15,'Jogo de adivinhação',' '*15)
print('='*50)

while True:

    computador = random.randint(0,5)

    jogador = int(input('Informe um numero de 0 a 5: '))

    if jogador > 5:
        print('Némero informa é maior que 5, tente novamente!')

    else:
        if computador == jogador:
            print(f'O numero gerado foi {computador}, parabéns você venceu!!!')
            break

        else:
            print(f'O numero gerado foi {computador} e o numero escolhido foi {jogador}, infelizmente você perdeu!!!')


