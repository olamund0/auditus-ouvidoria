from classe import *


def listarportipo(conexao):
    tipo = int(input('Que tipo de manifestação deseja exibir?'
                     '\n1)Elogio \n2)Reclamação \n3)Sugestão \n4)Voltar para o menu \nDigite: '))
    if tipo == 1:
        elogio = 'select count(*) from manifestacao where tipo = "Elogio" '
        manifestacao = listarBancoDados(conexao, elogio)
        quantidade = manifestacao[0][0]

        if quantidade == 0:
            print('Não existem elogios cadastrados!')
        else:
            print('------------Elogios------------')
            elogio = 'select * from manifestacao where tipo = "Elogio" '
            manifestacao = listarBancoDados(conexao, elogio)
            for i in manifestacao:
                print('Código', i[0], '-', i[1], '-', i[4], '-', 'Data:', i[5])

    elif tipo == 2:
        reclamacao = 'select count(*) from manifestacao where tipo = "Reclamação" '
        manifestacao = listarBancoDados(conexao, reclamacao)
        quantidade = manifestacao[0][0]

        if quantidade == 0:
            print('Não existem reclamações cadastradas!')
        else:
            print('------------Reclamações------------')
            reclamacao = 'select * from manifestacao where tipo = "Reclamação" '
            manifestacao = listarBancoDados(conexao, reclamacao)
            for i in manifestacao:
                print('Código', i[0], '-', i[1], '-', i[4], '-', 'Data:', i[5])

    elif tipo == 3:
        sugestao = 'select count(*) from manifestacao where tipo = "Sugestão" '
        manifestacao = listarBancoDados(conexao, sugestao)
        quantidade = manifestacao[0][0]

        if quantidade == 0:
            print('Não existem sugestões cadastradas!')
        else:
            print('------------Sugestões------------')
            sugestao = 'select * from manifestacao where tipo = "Sugestão" '
            manifestacao = listarBancoDados(conexao, sugestao)
            for i in manifestacao:
                print('Código', i[0], '-', i[1], '-', i[4], '-', 'Data:', i[5])

    elif tipo == 4:
        print('Menu')

    else:
        print('Opção inválida')
