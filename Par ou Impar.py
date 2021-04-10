from random import randint
import os
cont = vitorias = derrotas = 0

def menu_continuar():
    print("""
    Quer continuar a jogar?

    [1] Sim
    [2] Não

    """)

def limpa():
  os.system('cls' if os.name == 'nt' else 'clear')

def algoErrado():
    limpa()
    print('Algo deu errado aperte enter para continuar: ')
    input()

def ganhou():
    print("""
\033[1;34m              (☞ﾟヮﾟ)☞
              Parabéns 
            Você venceu!\033[m
            
            """)

def perdeu():
    print("""

\033[1;31m                ♨_♨

              Que pena
            Você perdeu!\033[m
            
            """)


while True:
    try:
        limpa()

        print("""
\033[1;32m            *****************************
            *       Par ou Ímpar        *
            *****************************\033[m

            Escolha a sua jogada:
            (1) Par
            (2) Ímpar

        """)

        par_ou_impar = input('Informe sua resposta: ')
        print(' ')
        jogador = int(input('Informe um valor de 0 a 10: '))
        print(' ')
        computador = randint(0,10)
        total = jogador + computador
        print(f"""
        
            Você jogo o número {jogador}
            Computador jogou o número {computador} 
            
            O total da jogada deu {total}
        
        """)

        if par_ou_impar == '1':
            if total %2 == 0:
                ganhou()
                vitorias +=1
                cont += 1
                menu_continuar()
                opcao = input('Informe se deseja continuar jogando: ')
                    
                if opcao == '2':
                    break
                elif opcao == '1':
                    continue
                else:
                    algoErrado()
                    
            elif total %2 != 0:
                perdeu()
                cont += 1
                derrotas +=1
                menu_continuar() 
                opcao = input('Informe se deseja continuar jogando: ')
                    
                if opcao == '2':
                    break
                elif opcao == '1':
                    continue
                else:
                    algoErrado()
                    
        elif par_ou_impar == '2':
            if total %2 != 0:
                ganhou()
                vitorias +=1
                cont += 1
                menu_continuar() 
                opcao = input('Informe se deseja continuar jogando: ')
                    
                if opcao == '2':
                    break
                elif opcao == '1':
                    continue
                else:
                    algoErrado()

            elif total %2 == 0:
                perdeu()
                cont += 1
                derrotas +=1
                menu_continuar() 
                opcao = input('Informe se deseja continuar jogando: ')
                    
                if opcao == '2':
                    break
                elif opcao == '1':
                    continue
                else:
                    algoErrado()

            else:
                algoErrado()

        else:
                algoErrado()
    except:
        algoErrado()

limpa()
print(f"""

\033[1;31m*********************************************************************************
*                 Game Over! Você jogou {cont} vezes, venceu {vitorias} e perdeu {derrotas}            *
*********************************************************************************\033[m

""")
