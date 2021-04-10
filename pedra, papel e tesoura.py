import random, os
from time import sleep

def limpa():
  os.system('cls' if os.name == 'nt' else 'clear')

def empate():
    print("""
                        
                → EMPATE ←

                """)

def vitoria():
    print("""

                \(￣︶￣*\))

                Você VENCEU 
                 Parabéns!

                """)

def derrota():
    print("""

                 ㄟ( ▔, ▔ )ㄏ

                  Você PERDEU 
                Tente novamente!

                """)

def algoErrado():
    limpa()
    print('Algo deu errado aperte enter para continuar: ')
    input()

while True:

    try:
        limpa()

        print("""

\033[1;32m            *****************************************************
            *                       Jokenpô                     *
            *****************************************************\033[m       
        """)

        itens = (' ', 'Pedra', 'Papel', 'Tesoura')

        print("""
                            Escolha uma jogada:

                                (1) Pedra
                                (2) Papel
                                (3) Tesoura

        """)

        jogada = int(input('Informe o número da sua jogada: '))

        computador = random.randint(1,3)
        print(' ')
        print("||                   Pedra                   ||\n")
        sleep(1)
        print("||                   Papel                   ||\n")
        sleep(1)
        print("||                 Tesoura!!!                ||\n")

        print()

        print('Jogada computador: {}'.format(itens[computador]))
        print('Sua jogada: {}'.format(itens[jogada]))

        print()

        if computador == 1:
            if jogada == 1:
                empate()

            elif jogada == 2:        
                vitoria()

            elif jogada == 3:
                derrota()

            else:
                algoErrado()

        elif computador == 2:
            if jogada == 1:
                derrota()
                

            elif jogada == 2:
                empate()
                
            elif jogada == 3:
                vitoria()

            else:
                algoErrado()

        elif computador == 3:
            if jogada == 1:
                vitoria()       

            elif jogada == 2:
                derrota()       

            elif jogada == 3:
                empate()

            else:
                algoErrado()

        else:
            algoErrado()

        print("""

            Quer continuar jogando?

            (1)Sim
            (2)Não

        """)

        continuar = input('    Informe sua resposta: ')

        if continuar == "2":
            limpa()
            print("""

            ************************************************************
            *          Ok, obrigada por jogar e até a próxima          *
            ************************************************************

            """)
            break
        
        elif continuar == "1":
            continue

        else:
            algoErrado()

    except:
        limpa()
        algoErrado()