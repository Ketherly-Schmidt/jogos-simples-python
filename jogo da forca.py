import os
import re
import getpass

arq = open("forca.txt","a")

def limpa():
  os.system('cls' if os.name == 'nt' else 'clear')

def caracterInvalidos(palavra):

  pattern = re.compile("[0-9]")
  erros = re.findall(pattern, palavra)

  if(len(erros) > 0):
    
    plural = ''
    pluraldois = ''
    if(len(erros) > 1):
      plural = 's'
      pluraldois = 'es'

    encontrados = 'O' + plural + ' caracter' + pluraldois + ' '
    for i in range(0, len(erros)):
      encontrados = encontrados + erros[i] + ' '
    
    encontrados = encontrados + ' não é permitido'

    return encontrados
  
  return True

while True:
  contDicas = 0
  try:

    print("""

    ********************************************
    *              Jogo Da Forca               *
    ********************************************

    """)

    palavra = getpass.getpass('Informe a palavra chave do jogo: ')
    
    contemErro = caracterInvalidos(palavra)
    if(contemErro != True):
      print(contemErro)
      continue
    
    limpa()

    nomeDesafiante = input("Informe o nome do desafiante: ")
    limpa()
    nomeCompetidor = input ('Informe o nome do competidor: ')
    limpa()


    dica = []
    for i in range (0,3):
      dica.append(getpass.getpass('Escreva uma dica: '))

    limpa()

    for x in range(1):
        print()
    digitadas = []
    acertos = []
    erros = 0

    while True:
      senha = ""
      for letra in palavra:
        senha += letra if letra in acertos else "*"
      print("""

      ********************************************
      *              Jogo Da Forca               *
      ********************************************

      """)
      print(f'Senha: {senha}')

      if senha == palavra:
        print("""
        
      ################################################
      #            parabéns você acertou!            #
      ################################################
        
        """)
        arq.write (f'A palavra é {palavra}')
        arq.write (f' O perdedor é o desafiante {nomeDesafiante}')
        arq.write (f' O Vencedor é o Competidor {nomeCompetidor}')
        arq.close()
        input()
        break
      else:

        print("""
        1 - dica
        2 - Tentar uma letra
        """)
        tentativa = ''
        resp1 = input("Informe a opção desejada: ")

        if resp1 == "1":
          if contDicas > 2:
            limpa()
            print("Vc não tem mais dicas")
            print('')
          else:
            limpa()
            print("A dica é: {}".format(dica[contDicas]))
            contDicas = contDicas  + 1

        elif resp1 == "2":
          tentativa = input("\nDigite uma letra: ").lower().strip()
          limpa()

        else:
          limpa()
          print('Resposta invalida, tente novamente!')         
          continue
          
        if tentativa in digitadas:
          limpa()
          print("Você já tentou esta letra!")         
          continue
        else:
          digitadas += tentativa
          if tentativa in palavra:
              acertos += tentativa
          else:
            erros += 1
            print("Você errou!")
            print('')
        if erros == 1:
          print(f"""
          
          Você já tem {erros} erros ╰（‵□′）╯
          ____
          |   |
          |   O
          |       |
          |       |
          |_______|

          Tente novamente, tome cuidado!

          """)         
        if erros == 2:
          print(f"""
          
          Você já tem {erros} erros ( ˘︹˘ )
          ____
          |   |
          |   O
          |   |   |
          |       |
          |_______|

          Tente novamente, tome cuidado!

          """)
                
        elif erros == 3:
          print(f"""
          
          Você já tem {erros} erros ＞﹏＜
          ____
          |   |
          |   O
          |  /|   |
          |       |
          |_______|

          Tente novamente e tome cuidado!

          """)
                
        elif erros == 4:

          print(f"""
          
          Você já tem {erros} erros (￣┰￣*)
          ____
          |   |
          |   O
          |  /|\  |
          |       |
          |_______|

          Tente novamente e tome muito cuidado!

          """)
                  
        if erros == 5:

          print(f"""
          
          Você já tem {erros} erros
          
          Está quase morrendo...

          ＼（〇_ｏ）／
          ____
          |   |
          |   O
          |  /|\  |
          |  /    |
          |_______|

          """)

                  
        elif erros >= 6:
          print(f"""
          
          Você já tem {erros} erros
          
          Que pena!!! Foi Enforcado!

          ¯\_(ツ)_/¯
          ____
          |   |
          |   O
          |  /|\  |
          |  / \  |
          |_______|

          """)
          arq.write (f'A palavra é {palavra}')
          arq.write (f' O vencedor é o desafiante {nomeDesafiante}')
          arq.write (f' O perdedor é o Competidor {nomeCompetidor}')
          arq.close()
          break

    print("""

    Deseja jogar novamente?

    (1) Sim 
    (2) Não

    """)

    resposta = input('    Informe sua resposta: ')
    limpa()
    if resposta == "2":
        limpa()
        print("""

        ************************************************************
        *       Ok, obrigada por participar e até a próxima        *
        ************************************************************

        """)
        break
    elif resposta == '1':
        print('Vamos começar mais uma partida, prepare-se!')
        limpa()

  except:
    print('Valor inválido')