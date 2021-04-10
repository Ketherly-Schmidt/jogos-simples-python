import random

print('='*50)
print(' '*15,'Jogo de adivinhação',' '*15)
print('='*50)

numero = random.randint(0,5)
while True:
    escolhido = int(input('Informe um numero de 0 a 5: '))

    if escolhido > 5:
        print('O número escolhido é maior que 5, tente novamente')

    else:
        if numero == escolhido:
            print(f'O numero gerado foi {numero}, parabéns você venceu!!!')
            break
            
        else:
            print(f'O numero gerado foi {numero} e o numero escolhido foi {escolhido}, infelizmente você perdeu!!!')
            break