import random

print('='*50)
print(' '*15,'Jogo de adivinhação',' '*15)
print('='*50)

computador = random.randint(0,5)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Informe um numero de 0 a 5: '))
    palpites += 1

    if jogador > 5:
        print('Némero informa é maior que 5, tente novamente!')

    else:
        if jogador == computador:
            acertou = True
        
        else:
            if jogador < computador:
                print('O numero jogado pelo computador é maior, tente novamente')
            
            elif jogador > computador:
                print('O numero jogado pelo computador é menor, tente novamente')

print(f'O numero gerado foi {computador}, parabéns você venceu!!!')


