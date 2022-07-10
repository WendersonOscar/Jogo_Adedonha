from random import randint 
valor = int(input('DIGITE UM VALOR: ')) #NÚMERO DO JOGADOR
opcao = str(input('IMPA OU PAR? [I/P]: ')).strip().upper()[0]
computador = randint(1, 10) #NÚMERO DO COMPUTADOR
cont = 0 #CONTADOR
while True:
    if opcao == 'P': #OPÇÃO ESCOLHIDA DO JOGADOR
        if (valor + computador) % 2:  #SABER SE É IMPAR OU PAR
            print(f'VOCÊ JOGOU {valor}, O COMPUTADOR JOGOU {computador}. TOTAL DE {valor+computador} ')
            print('você perdeu')
            break
        else:
            print(f'VOCÊ JOGOU {valor}, O COMPUTADOR JOGOU {computador}. TOTAL DE {valor+computador} ')
            print('VOCẼ VENCEU')
            cont += 1 #QUANTIDADE DE VEZES VENCIDAS
            valor = valor = int(input('número: '))
            opcao = opcao = str(input('OPÇÃo [i/p]: ')).strip().upper()[0]
    if opcao == 'I':
        if (valor + computador) % 2:
            print(f'VOCÊ JOGOU {valor}, O COMPUTADOR JOGOU {computador}. TOTAL DE {valor+computador} ')
            print('VOCÊ VENCEU')
            cont += 1
            valor = valor = int(input('número: '))
            opcao = opcao = str(input('OPÇÃo [i/p]: ')).strip().upper()[0]
        else:
            print(f'VOCÊ JOGOU {valor}, O COMPUTADOR JOGOU {computador}. TOTAL DE {valor+computador} ')
            print('você perdeu')
            break
if cont >1:
    print(f'VOCÊ TEVE {cont} Vitorias consecutivas!')
