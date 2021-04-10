import random
import os
from datetime import datetime, timedelta
from time import sleep

now = datetime.now()

arq = open("truco.txt","a")

def limpa():
  os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    input('\033[1;32mAperte Enter para continuar...\033[m')
    limpa()

def continuarPartida():
    print("""
    
    Deseja continuar jogando?

    (1)Sim
    (2)Não

    """)

def pontos():
    print ('')
    print ('         Rodada: %d'%rodada)
    print ('         Pontos Jogador na rodada: %d'%pontosjogadorrodada)
    print ('         Pontos PC na rodada: %d'%pontospcrodada)
    print(' ')
    print ('                        ------------Partida------------')
    print ('                        Jogador:   %d   PC:   %d' %(pontosjogadorpartida,pontospcpartida))
    print ('')


try:
  while True:

    print("""

    ****************************
    *          Truco           *
    ****************************      
    """)



    jogador = input('Informe seu nome: ')
    print()
    print('Olá \033[1;32m{}\033[m espero que esteja preparado(a), pois vamos comaçar em...'.format(jogador))
    print(' ')
    print('             → 1 ←')
    print(' ')
    sleep(1)
    print('             → 2 ←')
    print(' ')
    sleep(1)
    print('             → 3 ←')
    print(' ')
    sleep(1)
    print('              Já...')

    cartajogador1=1
    cartajogador2=1
    cartajogador3=1
    cartapc1=1
    cartapc2=1
    cartapc3=1
    sorteio=1
    opcaojogador1=1
    opcaojogador2=1
    opcaojogador3=1
    opcaopc1=1
    opcaopc2=1
    opcaopc3=1
    jogadapc=1 
    pergunta='d'
    pontospcpartida=0
    pontosjogadorpartida=0
    pontospcrodada=0
    pontosjogadorrodada=0
    rodada=0
    cartaescolhida=0
    forcajogador1=0
    forcajogador2=0
    forcajogador3=0
    forcapc1=0
    forcapc2=0
    forcapc3=0

    while pontospcpartida<12 and pontosjogadorpartida<12:
      opcaojogador1=1
      opcaojogador2=1
      opcaojogador3=1
      opcaopc1=1
      opcaopc2=1
      opcaopc3=1
      pontospcrodada=0
      pontosjogadorrodada=0
      rodada=0
      cartajogador1=1
      cartajogador2=1
      cartajogador3=1
      cartapc1=1
      cartapc2=1
      cartapc3=1
      sorteio=1
      
      print ("""
      
\033[1;35m                    ㄟ( ▔, ▔ )ㄏ

      O que foi? Embaralhar as cartas demora ué...\033[m
      
      """)
      sleep(2)

      while pontospcrodada < 2 and pontosjogadorrodada < 2:
          pergunta= 'd'
          cartaescolhida=0   

          while cartajogador1==cartajogador2 or cartajogador1==cartajogador3 or cartajogador2==cartajogador3 or sorteio==cartajogador1 or sorteio==cartajogador2 or sorteio ==cartajogador3 or cartajogador1==sorteio+1 or cartajogador1==sorteio+11 or cartajogador1==sorteio+21 or cartajogador1==sorteio+31 or cartajogador2==sorteio+1 or cartajogador2==sorteio+11 or cartajogador2==sorteio+21 or cartajogador2==sorteio+31 or cartajogador3==sorteio+1 or cartajogador3==sorteio+11 or cartajogador3==sorteio+21 or cartajogador3==sorteio+31 or cartajogador1==sorteio-9 or cartajogador1==sorteio-19 or cartajogador1==sorteio-29 or cartajogador1==sorteio-39 or cartajogador2==sorteio-9 or cartajogador2==sorteio-19 or cartajogador2==sorteio-29 or cartajogador2==sorteio-39 or cartajogador3==sorteio-9 or cartajogador3==sorteio-19 or cartajogador3==sorteio-29 or cartajogador3==sorteio-39 or cartapc1==cartapc2 or cartapc1==cartapc3 or cartapc2==cartapc3 or sorteio==cartapc1 or sorteio==cartapc2 or sorteio==cartapc3 or cartapc1==sorteio+1 or cartapc1==sorteio+11 or cartapc1==sorteio+21 or cartapc1==sorteio+31 or cartapc2==sorteio+1 or cartapc2==sorteio+11 or cartapc2==sorteio+21 or cartapc2==sorteio+31 or cartapc3==sorteio+1 or cartapc3==sorteio+11 or cartapc3==sorteio+21 or cartapc3==sorteio+31 or cartapc1==sorteio-9 or cartapc1==sorteio-19 or cartapc1==sorteio-29 or cartapc1==sorteio-39 or cartapc2==sorteio-9 or cartapc2==sorteio-19 or cartapc2==sorteio-29 or cartapc2==sorteio-39 or cartapc3==sorteio-9 or cartapc3==sorteio-19 or cartapc3==sorteio-29 or cartapc3==sorteio-39 or cartajogador1==cartapc1 or cartajogador1==cartapc2 or cartajogador1==cartapc3 or cartajogador2==cartapc1 or cartajogador2==cartapc2 or cartajogador2==cartapc3 or cartajogador3==cartapc1 or cartajogador3==cartapc2 or cartajogador3==cartapc3:

            cartajogador1 = random.randint(1,44)
            cartajogador2 = random.randint(1,44)
            cartajogador3 = random.randint(1,44)
            sorteio = random.randint(1,40)
            cartapc1 = random.randint(1,44)
            cartapc2 = random.randint(1,44)
            cartapc3 = random.randint(1,44)

          if cartajogador1==1:                 
            y='4 de Ouro'
            forcajogador1=1

          if cartajogador2==1:
            z='4 de Ouro'
            forcajogador2=1

          if cartajogador3==1:
            w='4 de Ouro'
            forcajogador3=1

          if sorteio==1:
            t='4 de Ouro'

          if cartajogador1==2:                 
            y='5 de Ouro'
            forcajogador1=5
          
          if cartajogador2==2:
            z='5 de Ouro'
            forcajogador2=5

          if cartajogador3==2:
            w='5 de Ouro'
            forcajogador3=5

          if sorteio==2:
            t='5 de Ouro'

          if cartajogador1==3:                 
            y='6 de Ouro'
            forcajogador1=9
          
          if cartajogador2==3:
            z='6 de Ouro'
            forcajogador2=9

          if cartajogador3==3:
            w='6 de Ouro'
            forcajogador3=9

          if sorteio==3:
            t='6 de Ouro'

          if cartajogador1==4:                 
            y='7 de Ouro'
            forcajogador1=13
        
          if cartajogador2==4:
            z='7 de Ouro'
            forcajogador2=13

          if cartajogador3==4:
            w='7 de Ouro'
            forcajogador3=13

          if sorteio==4:
            t='7 de Ouro'

          if cartajogador1==5:                 
            y='Dama de Ouro'
            forcajogador1=17  
      
          if cartajogador2==5:
            z='Dama de Ouro'
            forcajogador2=17

          if cartajogador3==5:
            w='Dama de Ouro'
            forcajogador3=17

          if sorteio==5:
            t='Dama de Ouro'

          if cartajogador1==6:                 
            y='Valete de Ouro'
            forcajogador1=21
          
          if cartajogador2==6:
            z='Valete de Ouro'
            forcajogador2=21

          if cartajogador3==6:
            w='Valete de Ouro'
            forcajogador3=21

          if sorteio==6:
            t='Valete de Ouro'

          if cartajogador1==7:                 
            y='Reis de Ouro'
            forcajogador1=25   
      
          if cartajogador2==7:
            z='Reis de Ouro'
            forcajogador2=25

          if cartajogador3==7:
            w='Reis de Ouro'
            forcajogador3=25

          if sorteio==7:
            t='Reis de Ouro'

          if cartajogador1==8:                 
            y='As de Ouro'
            forcajogador1=29
          
          if cartajogador2==8:
            z='As de Ouro'
            forcajogador2=29

          if cartajogador3==8:
            w='As de Ouro'
            forcajogador3=29

          if sorteio==8:
            t='As de Ouro'
      
          if cartajogador1==9:                 
            y='2 de Ouro'
            forcajogador1=33   
      
          if cartajogador2==9:
            z='2 de Ouro'
            forcajogador2=33

          if cartajogador3==9:
            w='2 de Ouro'
            forcajogador3=33

          if sorteio==9:
            t='2 de Ouro'

          if cartajogador1==10:                 
            y='3 de Ouro'
            forcajogador1=37
          
          if cartajogador2==10:
            z='3 de Ouro'
            forcajogador2=37

          if cartajogador3==10:
            w='3 de Ouro'
            forcajogador3=37

          if sorteio==10:
            t='3 de Ouro'

          if cartajogador1==41:                 
            y='Sete Ouro'
          forcajogador1=41
          
          if cartajogador2==41:
            z='Sete Ouro'
            forcajogador2=41

          if cartajogador3==41:
            w='Sete Ouro'
            forcajogador3=41

          if sorteio==41:
            t='5 de Espada'

          if cartajogador1==11:                 
            y='4 de Espada'
            forcajogador1=2

          if cartajogador2==11:
            z='4 de Espada'
            forcajogador2=2

          if cartajogador3==11:
            w='4 de Espada'
            forcajogador3=2
      
          if sorteio==11:
            t='4 de Espada'

          if cartajogador1==12:                 
            y='5 de Espada'
            forcajogador1=6   
      
          if cartajogador2==12:
            z='5 de Espada'
            forcajogador2=6

          if cartajogador3==12:
            w='5 de Espada'
            forcajogador3=6

          if sorteio==12:
            t='5 de Espada'

          if cartajogador1==13:                 
            y='6 de Espada'
            forcajogador1=10
          
          if cartajogador2==13:
            z='6 de Espada'
            forcajogador2=10

          if cartajogador3==13:
            w='6 de Espada'
            forcajogador3=10

          if sorteio==13:
            t='6 de Espada'

          if cartajogador1==14:                 
            y='7 de Espada'
            forcajogador1=14   
      
          if cartajogador2==14:
            z='7 de Espada'
            forcajogador2=14
      
          if cartajogador3==14:
            w='7 de Espada'
            forcajogador3=14

          if sorteio==14:
            t='7 de Espada'

          if cartajogador1==15:                 
            y='Dama de Espada'
            forcajogador1=18
          
          if cartajogador2==15:
            z='Dama de Espada'
            forcajogador2=18

          if cartajogador3==15:
            w='Dama de Espada'
            forcajogador3=18

          if sorteio==15:
            t='Dama de Espada'

          if cartajogador1==16:                 
            y='Valete de Espada'
            forcajogador1=22
          
          if cartajogador2==16:
            z='Valete de Espada'
            forcajogador2=22

          if cartajogador3==16:
            w='Valete de Espada'
            forcajogador3=22

          if sorteio==16:
            t='Valete de Espada'

          if cartajogador1==17:                 
            y='Reis de Espada'
            forcajogador1=26   
      
          if cartajogador2==17:
            z='Reis de Espada'
            forcajogador2=26

          if cartajogador3==17:
            w='Reis de Espada'
            forcajogador3=26

          if sorteio==17:
            t='Reis de Espada'

          if cartajogador1==18:                 
            y='As de Espada'
            forcajogador1=30
          
          if cartajogador2==18:
            z='As de Espada'
            forcajogador2=30

          if cartajogador3==18:
            w='As de Espada'
            forcajogador3=30

          if sorteio==18:
            t='As de Espada'

          if cartajogador1==19:                 
            y='2 de Espada'
            forcajogador1=34   
      
          if cartajogador2==19:
            z='2 de Espada'
            forcajogador2=34

          if cartajogador3==19:
            w='2 de Espada'
            forcajogador3=34

          if sorteio==19:
            t='2 de Espada'   

          if cartajogador1==20:                 
            y='3 de Espada'
            forcajogador1=38
          
          if cartajogador2==20:
            z='3 de Espada'
            forcajogador2=38

          if cartajogador3==20:
            w='3 de Espada'
            forcajogador3=38

          if sorteio==20:
            t='3 de Espada'
      
          if cartajogador1==42:                 
            y='Espadilha'
            forcajogador1=42

          if cartajogador2==42:
            z='Espadilha'
            forcajogador2=42

          if cartajogador3==42:
            w='Espadilha'
            forcajogador3=42

          if sorteio==42:
            t='7 de Copa'
          
          if cartajogador1==21:                 
            y='4 de Copa'
            forcajogador1=3

          if cartajogador2==21:
            z='4 de Copa'
            forcajogador2=3

          if cartajogador3==21:
            w='4 de Copa'
            forcajogador3=3

          if sorteio==21:
            t='4 de Copa'

          if cartajogador1==22:                 
            y='5 de Copa'
            forcajogador1=7      
      
          if cartajogador2==22:
            z='5 de Copa'

            forcajogador2=7

          if cartajogador3==22:
            w='5 de Copa'
            forcajogador3=7

          if sorteio==22:
            t='5 de Copa'

          if cartajogador1==23:                 
            y='6 de Copa'
            forcajogador1=11
          
          if cartajogador2==23:
            z='6 de Copa'
            forcajogador2=11

          if cartajogador3==23:
            w='6 de Copa'
            forcajogador3=11

          if sorteio==23:
            t='6 de Copa'
            forcajogador1=11

          if cartajogador1==24:                 
            y='7 de Copa'
            forcajogador1=15
          
          if cartajogador2==24:
            z='7 de Copa'
            forcajogador2=15

          if cartajogador3==24:
            w='7 de Copa'
            forcajogador3=15

          if sorteio==24:
            t='7 de Copa'

          if cartajogador1==25:                 
            y='Dama de Copa'
            forcajogador1=19   
      
          if cartajogador2==25:
            z='Dama de Copa'
            forcajogador2=19

          if cartajogador3==25:
            w='Dama de Copa'
            forcajogador3=19
      
          if sorteio==25:
            t='Dama de Copa'

          if cartajogador1==26:                 
            y='Valete de Copa'   
            forcajogador1=23   
          
          if cartajogador2==26:
            z='Valete de Copa'
            forcajogador2=23

          if cartajogador3==26:
            w='Valete de Copa'
            forcajogador3=23

          if sorteio==26:
            t='Valete de Copa'

          if cartajogador1==27:                 
            y='Reis de Copa'
            forcajogador1=27   
      
          if cartajogador2==27:
            z='Reis de Copa'
            forcajogador2=27

          if cartajogador3==27:
            w='Reis de Copa'
            forcajogador3=27

          if sorteio==27:
            t='Reis de Copa'

          if cartajogador1==28:                 
            y='As de Copa'
            forcajogador1=31   
      
          if cartajogador2==28:
            z='As de Copa'
            forcajogador2=31

          if cartajogador3==28:
            w='As de Copa'
            forcajogador3=31

          if sorteio==28:
            t='As de Copa'   

          if cartajogador1==29:                 
            y='2 de Copa'
            forcajogador1=35
            
          if cartajogador2==29:
            z='2 de Copa'
            forcajogador2=35

          if cartajogador3==29:
            w='2 de Copa'
            forcajogador3=35

          if sorteio==29:
            t='2 de Copa'

          if cartajogador1==30:                 
            y='3 de Copa'
            forcajogador1=39
          
          if cartajogador2==30:
            z='3 de Copa'
            forcajogador2=39

          if cartajogador3==30:
            w='3 e Copa'
            forcajogador3=39

          if sorteio==30:
            t='3 de Copa'

          if cartajogador1==43:                 
            y='Sete Copa'
            forcajogador1=43

          if cartajogador2==43:
            z='Sete Copa'
            forcajogador2=43

          if cartajogador3==43:
            w='Sete Copa'
            forcajogador3=43

          if sorteio==43:
            t='4 de Paus'

          if cartajogador1==31:                 
            y='4 de Paus'
            forcajogador1=4

          if cartajogador2==31:
            z='4 de Paus'
            forcajogador2=4

          if cartajogador3==31:
            w='4 de Paus'
            forcajogador3=4

          if sorteio==31:
            t='4 de Paus'
            forcajogador1=4

          if cartajogador1==32:                 
            y='5 de Paus'
            forcajogador1=8      
      
          if cartajogador2==32:
            z='5 de Paus'
            forcajogador2=8

          if cartajogador3==32:
            w='5 de Paus'
            forcajogador3=8

          if sorteio==32:
            t='5 de Paus'

          if cartajogador1==33:                 
            y='6 de Paus'
            forcajogador1=12
          
          if cartajogador2==33:
            z='6 de Paus'
            forcajogador2=12

          if cartajogador3==33:
            w='6 de Paus'
            forcajogador3=12

          if sorteio==33:
            t='6 de Paus'

          if cartajogador1==34:                 
            y='7 de Paus'
            forcajogador1=16   
      
          if cartajogador2==34:
            z='7 de Paus'
            forcajogador2=16

          if cartajogador3==34:
            w='7 de Paus'
            forcajogador3=16

          if sorteio==34:
            t='7 de Paus'

          if cartajogador1==35:                 
            y='Dama de Paus'
            forcajogador1=20   
      
          if cartajogador2==35:
            z='Dama de Paus'
            forcajogador2=20

          if cartajogador3==35:
            w='Dama de Paus'
            forcajogador3=20

          if sorteio==35:
            t='Dama de Paus'

          if cartajogador1==36:                 
            y='Valete de Paus'
            forcajogador1=24   
      
          if cartajogador2==36:
            z='Valete de Paus'
            forcajogador2=24

          if cartajogador3==36:
            w='Valete de Paus'
            forcajogador3=24

          if sorteio==36:
            t='Valete de Paus'

          if cartajogador1==37:                 
            y='Reis de Paus'
            forcajogador1=28
          
          if cartajogador2==37:
            z='Reis de Paus'
            forcajogador2=28

          if cartajogador3==37:
            w='Reis de Paus'
            forcajogador3=28

          if sorteio==37:
            t='Reis de Paus'

          if cartajogador1==38:                 
            y='As de Paus'
            forcajogador1=32   
      
          if cartajogador2==38:
            z='As de Paus'
            forcajogador2=32

          if cartajogador3==38:
            w='As de Paus'
            forcajogador3=32

          if sorteio==38:
            t='As de Paus'

          if cartajogador1==39:                 
            y='2 de Paus'
            forcajogador1=36   
      
          if cartajogador2==39:
            z='2 de Paus'
            forcajogador2=36

          if cartajogador3==39:
            w='2 de Paus'
            forcajogador3=36

          if sorteio==39:
            t='2 de Paus'

          if cartajogador1==40:                 
            y='3 de Paus'
            forcajogador1=40
          
          if cartajogador2==40:
            z='3 de Paus'
            forcajogador2=40

          if cartajogador3==40:
            w='3 de Paus'
            forcajogador3=40

          if sorteio==40:
            t='3 de Paus'

          if cartajogador1==44:                 
            y='Zap'
            forcajogador1=44
      
          if cartajogador2==44:
            z='Zap'
            forcajogador2=44

          if cartajogador3==44:
            w='Zap'
            forcajogador3=44

          if sorteio==44:
            t='6 de Ouro'

          if cartapc1==1:                 
            yy='4 de Ouro'
            forcapc1=1   
      
          if cartapc2==1:
            zz='4 de Ouro'
            forcapc2=1

          if cartapc3==1:
            ww='4 de Ouro'
            forcapc3=1

          if cartapc1==2:                 
            yy='5 de Ouro'
            forcapc1=5
    
          if cartapc2==2:
            zz='5 de Ouro'
            forcapc2=5

          if cartapc3==2:
            www='5 de Ouro'
            forcapc3=5

          if cartapc1==3:                 
            yy='6 de Ouro'
            forcapc1=9
      
          if cartapc2==3:
            zz='6 de Ouro'
            forcapc2=9

          if cartapc3==3:
            ww='6 de Ouro'
            forcapc3=9

          if cartapc1==4:                 
            yy='7 de Ouro'
            forcapc1=13
      
          if cartapc2==4:
            zz='7 de Ouro'
            forcapc2=13

          if cartapc3==4:
            ww='7 de Ouro'
            forcapc3=13

          if cartapc1==5:                 
            yy='Dama de Ouro'
            forcapc1=17
      
          if cartapc2==5:
            zz='Dama de Ouro'
            forcapc2=17

          if cartapc3==5:
            ww='Dama de Ouro'
            forcapc3=17

          if cartapc1==6:                 
            yy='Valete de Ouro'
            forcapc1=21
      
          if cartapc2==6:
            zz='Valete de Ouro'
            forcapc2=21

          if cartapc3==6:
            ww='Valete de Ouro'
            forcapc3=21

          if cartapc1==7:                 
            yy='Reis de Ouro'
            forcapc1=25
      
          if cartapc2==7:
            zz='Reis de Ouro'
            forcapc2=25
      
          if cartapc3==7:
            ww='Reis de Ouro'
            forcapc3=25

          if cartapc1==8:                 
            yy='As de Ouro'
            forcapc2=29
      
          if cartapc2==8:
            zz='As de Ouro'
            forcapc3=29

          if cartapc3==8:
            ww='As de Ouro'
            forcapc2=29
      
          if cartapc1==9:                 
            yy='2 de Ouro'
            forcapc3=33
          
          if cartapc2==9:
            zz='2 de Ouro'
            forcapc2=33

          if cartapc3==9:
            ww='2 de Ouro'
            forcapc3=33

          if cartapc1==10:                 
            yy='3 de Ouro'
            forcapc1=37
      
          if cartapc2==10:
            zz='3 de Ouro'
            forcapc2=37

          if cartapc3==10:
            ww='3 de Ouro'
            forcapc3=37

          if cartapc1==41:                 
            yy='Sete Ouro'
            forcapc1=41
          
          if cartapc2==41:
            zz='Sete Ouro'
            forcapc2=41

          if cartapc3==41:
            ww='Sete Ouro'
            forcapc3=41

          if cartapc1==11:                 
            yy='4 de Espada'
            forcapc1=2
      
          if cartapc2==11:
            zz='4 de Espada'
            forcapc2=2

          if cartapc3==11:
            ww='4 de Espada'
            forcapc3=2

          if cartapc1==12:                 
            yy='5 de Espada'
            forcapc1=6
      
          if cartapc2==12:
            zz='5 de Espada'
            forcapc2=6

          if cartapc3==12:
            ww='5 de Espada'
            forcapc3=6

          if cartapc1==13:                 
            yy='6 de Espada'
            forcapc1=10
      
          if cartapc2==13:
            zz='6 de Espada'
            forcapc2=10

          if cartapc3==13:
            ww='6 de Espada'
            forcapc3=10

          if cartapc1==14:                 
            yy='7 de Espada'
            forcapc1=14
      
          if cartapc2==14:
            zz='7 de Espada'
            forcapc2=14

          if cartapc3==14:
            ww='7 de Espada'
            forcapc3=14

          if cartapc1==15:                 
            yy='Dama de Espada'
            forcapc1=18
      
          if cartapc2==15:
            zz='Dama de Espada'
            forcapc2=18

          if cartapc3==15:
            ww='Dama de Espada'
            forcapc3=18

          if cartapc1==16:                 
            yy='Valete de Espada'
            forcapc1=22
      
          if cartapc2==16:
            zz='Valete de Espada'
            forcapc2=22
      
          if cartapc3==16:
            ww='Valete de Espada'
            forcapc3=22
      
          if cartapc1==17:                 
            yy='Reis de Espada'
            forcapc1=26
      
          if cartapc2==17:
            zz='Reis de Espada'
            forcapc2=26

          if cartapc3==17:
            ww='Reis de Espada'
            forcapc3=26

          if cartapc1==18:                 
            yy='As de Espada'
            forcapc1=30
      
          if cartapc2==18:
            zz='As de Espada'
            forcapc2=30

          if cartapc3==18:
            ww='As de Espada'
            forcapc3=30

          if cartapc1==19:                 
            yy='2 de Espada'
            forcapc1=34
      
          if cartapc2==19:
            zz='2 de Espada'
            forcapc2=34

          if cartapc3==19:
            ww='2 de Espada'
            forcapc3=34

          if cartapc1==20:                 
            yy='3 de Espada'
            forcapc1=38
      
          if cartapc2==20:
            zz='3 de Espada'
            forcapc2=38

          if cartapc3==20:
            ww='3 de Espada'
            forcapc3=38

          if cartapc1==42:                 
            yy='Espadilha'
            forcapc1=42

          if cartapc2==42:
            zz='Espadilha'
            forcapc2=42

          if cartapc3==42:
            ww='Espadilha'
            forcapc3=42

          if cartapc1==21:                 
            yy='4 de Copa'
            forcapc1=3
      
          if cartapc2==21:
            zz='4 de Copa'
            forcapc2=3

          if cartapc3==21:
            ww='4 de Copa'
            forcapc3=3

          if cartapc1==22:                 
            yy='5 de Copa'
            forcapc1=7
      
          if cartapc2==22:
            zz='5 de Copa'
            forcapc2=7

          if cartapc3==22:
            ww='5 de Copa'
            forcapc3=7

          if cartapc1==23:                 
            yy='6 de Copa'
            forcapc1=11
      
          if cartapc2==23:
            zz='6 de Copa'
            forcapc2=11

          if cartapc3==23:
            ww='6 de Copa'
            forcapc3=11

          if cartapc1==24:                 
            yy='7 de Copa'
            forcapc1=15

          if cartapc2==24:
            zz='7 de Copa'
            forcapc2=15

          if cartapc3==24:
            ww='7 de Copa'
            forcapc3=15

          if cartapc1==25:                 
            yy='Dama de Copa'
            forcapc1=19
      
          if cartapc2==25:
            zz='Dama de Copa'
            forcapc2=19

          if cartapc3==25:
            ww='Dama de Copa'
            forcapc3=19

          if cartapc1==26:                 
            yy='Valete de Copa'
            forcapc1=23
      
          if cartapc2==26:
            zz='Valete de Copa'
            forcapc2=23

          if cartapc3==26:
            ww='Valete de Copa'
            forcapc3=23

          if cartapc1==27:                 
            yy='Reis de Copa'
            forcapc1=27
      
          if cartapc2==27:
            zz='Reis de Copa'
            forcapc2=27

          if cartapc3==27:
            ww='Reis de Copa'
            forcapc3=27

          if cartapc1==28:                 
            yy='As de Copa'
            forcapc1=31
      
          if cartapc2==28:
            zz='As de Copa'
            forcapc2=31

          if cartapc3==28:
            ww='As de Copa'
            forcapc3=31

          if cartapc1==29:                 
            yy='2 de Copa'
            forcapc1=35
      
          if cartapc2==29:
            zz='2 de Copa'
            forcapc2=35

          if cartapc3==29:
            ww='2 de Copa'
            forcapc3=35

          if cartapc1==30:                 
            yy='3 de Copa'
            forcapc1=39
            
          if cartapc2==30:
            zz='3 de Copa'
            forcapc2=39

          if cartapc3==30:
            ww='3 de Copa'
            forcapc3=39

          if cartapc1==43:                 
            yy='Sete Copa'
            forcapc1=43

          if cartapc2==43:
            zz='Sete Copa'
            forcapc2=43

          if cartapc3==43:
            ww='Sete Copa'
            forcapc3=43

          if cartapc1==31:                 
            yy='4 de Paus'
            forcapc1=4
            
          if cartapc2==31:
            zz='4 de Paus'
            forcapc2=4

          if cartapc3==31:
            ww='4 de Paus'
            forcapc3=4

          if cartapc1==32:                 
            yy='5 de Paus'
            forcapc1=8
      
          if cartapc2==32:
            zz='5 de Paus'
            forcapc2=8

          if cartapc3==32:
            ww='5 de Paus'
            forcapc3=8

          if cartapc1==33:                 
            yy='6 de Paus'
            forcapc1=12
      
          if cartapc2==33:
            zz='6 de Paus'
            forcapc2=12

          if cartapc3==33:
            ww='6 de Paus'
            forcapc3=12

          if cartapc1==34:                 
            yy='7 de Paus'
            forcapc1=16
          
          if cartapc2==34:
            zz='7 de Paus'
            forcapc2=16

          if cartapc3==34:
            ww='7 de Paus'
            forcapc3=16

          if cartapc1==35:                 
            yy='Dama de Paus'
            forcapc1=20
      
          if cartapc2==35:
            zz='Dama de Paus'
            forcapc2=20

          if cartapc3==35:
            ww='Dama de Paus'
            forcapc3=20

          if cartapc1==36:                 
            yy='Valete de Paus'
            forcapc1=24
      
          if cartapc2==36:
            zz='Valete de Paus'
            forcapc2=24

          if cartapc3==36:
            ww='Valete de Paus'
            forcapc3=24

          if cartapc1==37:                 
            yy='Reis de Paus'
            forcapc1=28
          
          if cartapc2==37:
            zz='Reis de Paus'
            forcapc2=28

          if cartapc3==37:
            ww='Reis de Paus'
            forcapc3=28

          if cartapc1==38:                 
            yy='As de Paus'
            forcapc1=32
      
          if cartapc2==38:
            zz='As de Paus'
            forcapc2=32

          if cartapc3==38:
            ww='As de Paus'
            forcapc3=32
      
          if cartapc1==39:                 
            yy='2 de Paus'
            forcapc1=36
      
          if cartapc2==39:
            zz='2 de Paus'
            forcapc2=36

          if cartapc3==39:
            ww='2 de Paus'
            forcapc3=36

          if cartapc1==40:                 
            yy='3 de Paus'
            forcapc1=40
      
          if cartapc2==40:
            zz='3 de Paus'
            forcapc2=40

          if cartapc3==40:
            ww='3 de Paus'
            forcapc3=40

          if cartapc1==44:                 
            yy='Zap'
            forcapc1=44

          if cartapc2==44:
            zz='Zap'
            forcapc2=44

          if cartapc3==44:
            ww='Zap'
            forcapc3=44
          
          print (""" 
\033[1;32m                Suas Cartas sorteadas são...\033[m            
          """ )
          print ('-'*30 + '|' + '-'*30 )
          print('⇨ Carta do baralho: %s' %t)
          print(' ')
          if opcaojogador1==1:  
            print ('⇨ Sua primeira carta(A) é a : %s'%y )
          if opcaojogador2==1:
            print ('⇨ Sua segunda carta(B) é a : %s' %z)
          if opcaojogador3==1:
            print ('⇨ Sua terceira carta(C) é a : %s'%w )

          escolhido = random.randint(1,2)
          
          if escolhido == 1:
            print(' ')
            print('É a vez do(a) Jogador(a) \033[1;32m{}\033[m'.format(jogador))

            while pergunta != 'a' and pergunta != 'b' and pergunta != 'c':
              
              if opcaojogador1==1 and opcaojogador2==1 and opcaojogador3==1:
                  while pergunta != 'a' and pergunta != 'b' and pergunta != 'c':
                    pergunta = str(input('Escolha uma carta para jogar:(a ou b ou c): '))
                    print(' ')
              elif opcaojogador1==1 and opcaojogador2==1 and opcaojogador3==0:
                  while pergunta != 'a' and pergunta != 'b':
                    print(' ')
                    pergunta = str(input('Escolha sua carta:(a ou b): '))
              elif opcaojogador1==1 and opcaojogador2==0 and opcaojogador3==0:
                  while pergunta != 'a':
                    print(' ')
                    pergunta = str(input('Você só pode escolher a carta A agora: '))
              elif opcaojogador1==0 and opcaojogador2==1 and opcaojogador3==0:
                  while pergunta != 'b':
                    print(' ')
                    pergunta = str(input('Você só pode escolhar a carta B agora: '))
              elif opcaojogador1==0 and opcaojogador2==0 and opcaojogador3==1:
                  while pergunta != 'c':
                    print(' ')
                    pergunta = str(input('Você só pode escolher a carta C agora:'))
              elif opcaojogador1==0 and opcaojogador2==1 and opcaojogador3==1:
                  while pergunta != 'b' and pergunta != 'c':
                    print(' ')
                    pergunta = str(input('Escolha sua carta:(b ou c): '))
              elif opcaojogador1==1 and opcaojogador2==0 and opcaojogador3==1:
                  while pergunta != 'a' and pergunta != 'c':
                    print(' ')
                    pergunta = str(input('Escolha sua carta:(a ou c): '))
                    print(' ')
            
            if pergunta=='a':
              print('   %s'%y)
              print(' ')
              cartaescolhida = forcajogador1
              opcaojogador1=0

            if pergunta=='b':
              print('    %s'%z)
              print(' ')
              cartaescolhida = forcajogador2
              opcaojogador2=0

            if pergunta=='c':
              print('     %s'%w)
              print(' ')
              cartaescolhida = forcajogador3
              opcaojogador3=0

            print ()
            print('\033[1;34mPC escolhendo...\033[m')

            if opcaopc1==1 and opcaopc2==1 and opcaopc3==1:
              if forcapc1>forcapc2 and forcapc1>forcapc3:
                  jogadapc = 1
              elif forcapc2>forcapc1 and forcapc2>forcapc3:
                  jogadapc = 2
              elif forcapc3>forcapc1 and forcapc3>forcapc2:
                  jogadapc = 3
              if cartaescolhida > forcapc1 and cartaescolhida > forcapc2 and cartaescolhida > forcapc3:
                  if forcapc1<forcapc2 and forcapc1<forcapc3:
                    jogadapc = 1
                  elif forcapc2<forcapc1 and forcapc2<forcapc3:
                    jogadapc = 2
                  elif forcapc3<forcapc1 and forcapc3<forcapc2:
                    jogadapc = 3

            elif opcaopc1==0 and opcaopc2==1 and opcaopc3==1:
              jogadapc = random.randint(2,3)
        
            elif opcaopc1==1 and opcaopc2==1 and opcaopc3==0:
              jogadapc = random.randint(1,2)

            elif opcaopc1==1 and opcaopc2==0 and opcaopc3==1:
              jogadapc = random.randint(1,3)
              while jogadapc == 2:
                  jogadapc = random.randint(1,3)

            elif opcaopc1==1 and opcaopc2==0 and opcaopc3==0:
              jogadapc = 1
        
            elif opcaopc1==0 and opcaopc2==1 and opcaopc3==0:
              jogadapc = 2

            elif opcaopc1==0 and opcaopc2==0 and opcaopc3==1:
              jogadapc = 3

            if jogadapc == 1:
              opcaopc1=0
              print(' ')
              print (' \033[1;34m⇒ PC jogou\033[m %s'%yy)

              if cartaescolhida < forcapc1:
                  pontospcrodada = pontospcrodada + 1
              else:
                  pontosjogadorrodada = pontosjogadorrodada + 1
            
              print ('')

            if jogadapc == 2:
              opcaopc2=0
              print(' ')
              print (' \033[1;34m⇒ PC jogou\033[m %s'%zz)

              if cartaescolhida < forcapc2:
                  pontospcrodada = pontospcrodada + 1
              else:
                  pontosjogadorrodada = pontosjogadorrodada + 1
              print ('')

            if jogadapc == 3:
              opcaopc3=0
              print(' ')
              print (' \033[1;34m⇒ PC jogou\033[m %s'%ww)

              if cartaescolhida < forcapc3:
                  pontospcrodada = pontospcrodada + 1
              else:
                  pontosjogadorrodada = pontosjogadorrodada + 1
              print ('')

            rodada = rodada + 1

            pontos()
                        
            if pontosjogadorrodada == 2:
              pontosjogadorpartida = pontosjogadorpartida + 1

            if pontospcrodada == 2:
              pontospcpartida = pontospcpartida + 1
            print ( )

            continuar()
          
          else:
            print("""
            
            \033[1;34mÉ a Vez do Pc jogar\033[m            
            """)
            while pergunta != 'a' and pergunta != 'b' and pergunta != 'c':

              sleep(2)
              print("""            
              \033[1;34mPC escolhendo...\033[m
            
              """)
              sleep(2)


              if opcaopc1==1 and opcaopc2==1 and opcaopc3==1:
                if forcapc1>forcapc2 and forcapc1>forcapc3:
                    jogadapc = 1
                elif forcapc2>forcapc1 and forcapc2>forcapc3:
                    jogadapc = 2
                elif forcapc3>forcapc1 and forcapc3>forcapc2:
                    jogadapc = 3
                if cartaescolhida > forcapc1 and cartaescolhida > forcapc2 and cartaescolhida > forcapc3:
                    if forcapc1<forcapc2 and forcapc1<forcapc3:
                      jogadapc = 1
                    elif forcapc2<forcapc1 and forcapc2<forcapc3:
                      jogadapc = 2
                    elif forcapc3<forcapc1 and forcapc3<forcapc2:
                      jogadapc = 3

              elif opcaopc1==0 and opcaopc2==1 and opcaopc3==1:
                jogadapc = random.randint(2,3)
          
              elif opcaopc1==1 and opcaopc2==1 and opcaopc3==0:
                jogadapc = random.randint(1,2)

              elif opcaopc1==1 and opcaopc2==0 and opcaopc3==1:
                jogadapc = random.randint(1,3)
                while jogadapc == 2:
                    jogadapc = random.randint(1,3)

              elif opcaopc1==1 and opcaopc2==0 and opcaopc3==0:
                jogadapc = 1
          
              elif opcaopc1==0 and opcaopc2==1 and opcaopc3==0:
                jogadapc = 2

              elif opcaopc1==0 and opcaopc2==0 and opcaopc3==1:
                jogadapc = 3

              if jogadapc == 1:
                opcaopc1=0
                print (""" 
           PC jogou %s
                               
                """%yy)
                if cartaescolhida < forcapc1:
                    pontospcrodada = pontospcrodada + 1
                else:
                    pontosjogadorrodada = pontosjogadorrodada + 1
              
                print ('')

              if jogadapc == 2:
                opcaopc2=0
                print (""" 
           \033[1;34m⇒ PC jogou\033[m %s
                
                """%zz)
                if cartaescolhida < forcapc2:
                    pontospcrodada = pontospcrodada + 1
                else:
                    pontosjogadorrodada = pontosjogadorrodada + 1
                print ('')

              if jogadapc == 3:
                opcaopc3=0
                print (""" 
           \033[1;34m⇒ PC jogou\033[m %s
                
                """%ww)
                if cartaescolhida < forcapc3:
                    pontospcrodada = pontospcrodada + 1
                else:
                    pontosjogadorrodada = pontosjogadorrodada + 1
                print ('')

              if opcaojogador1==1 and opcaojogador2==1 and opcaojogador3==1:
                    while pergunta != 'a' and pergunta != 'b' and pergunta != 'c':
                        print(' ')
                        pergunta = str(input('Escolha uma carta para jogar:(a ou b ou c): '))
              elif opcaojogador1==1 and opcaojogador2==1 and opcaojogador3==0:
                    while pergunta != 'a' and pergunta != 'b':
                      print(' ')
                      pergunta = str(input('Escolha sua carta:(a ou b): '))
              elif opcaojogador1==1 and opcaojogador2==0 and opcaojogador3==0:
                    while pergunta != 'a':
                      print(' ')
                      pergunta = str(input('Você só pode escolher a carta A agora: '))
              elif opcaojogador1==0 and opcaojogador2==1 and opcaojogador3==0:
                    while pergunta != 'b':
                      print(' ')
                      pergunta = str(input('Você só pode escolhar a carta B agora: '))
              elif opcaojogador1==0 and opcaojogador2==0 and opcaojogador3==1:
                    while pergunta != 'c':
                      print(' ')
                      pergunta = str(input('Você só pode escolher a carta C agora:'))
              elif opcaojogador1==0 and opcaojogador2==1 and opcaojogador3==1:
                    while pergunta != 'b' and pergunta != 'c':
                      print(' ')
                      pergunta = str(input('Escolha sua carta:(b ou c): '))
              elif opcaojogador1==1 and opcaojogador2==0 and opcaojogador3==1:
                    while pergunta != 'a' and pergunta != 'c':
                      print(' ')
                      pergunta = str(input('Escolha sua carta:(a ou c): '))
              
              if pergunta=='a':
                print(' ')
                print('   %s'%y)
                cartaescolhida = forcajogador1
                opcaojogador1=0

              if pergunta=='b':
                print(' ')
                print('    %s'%z)
                cartaescolhida = forcajogador2
                opcaojogador2=0

              if pergunta=='c':
                print(' ')
                print('     %s'%w)
                cartaescolhida = forcajogador3
                opcaojogador3=0

              print (' ')

              rodada = rodada + 1

              pontos()
             
              if pontosjogadorrodada == 2:
                pontosjogadorpartida = pontosjogadorpartida + 1

              if pontospcrodada == 2:
                pontospcpartida = pontospcpartida + 1
              print ( )

              continuar()
              
    if pontospcpartida >= 12:
        print("""
\033[1;31m                        ಥ_ಥ
                Que pena você perdeu!!!
        Mais sorte (ou habilidade) na proxíma vez...\033[m
      
      """)

        arq.write ('O Jogador(a) {} foi derrotado pela maquina \n'.format(jogador))
        arq.write ('fim de jogo')
        arq.close()

        continuarPartida()
        resposta = input('Informe sua resposta: ')

        if resposta == '1':
            continue

        elif resposta == '2':
            break

        else:
            print('Tente novamente')
      

    elif pontosjogadorpartida >=12:

        print("""
\033[1;32m                 ( ﾉ ﾟｰﾟ)ﾉ
                Parabéns!!!
        Você é o grande campeão!!!\033[m
      
      """)

        arq.write ('O Jogador(a) {} derrotou a maquina e é o grande vencedor.\n'.format(jogador))
        arq.write ('  fim de jogo')
        arq.close()
        print ('')

        continuarPartida()
        resposta = input('Informe sua resposta: ')

        if resposta == '1':
            continue

        elif resposta == '2':
            break

        else:
            print('Tente novamente')

    print("""

            ************************************************************
            *          Ok, obrigada por jogar e até a próxima          *
            ************************************************************

         """)
except:
  print('Valor inválido, tente novamente...')