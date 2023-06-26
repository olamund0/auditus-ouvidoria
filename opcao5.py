from classe import *


def pesquisarcodigo(conexao):
    codigo = input('Digite o código da manifestação que deseja exibir: ')
    consulta = 'select * from manifestacao where codigo = ' + codigo
    pesquisa = listarBancoDados(conexao, consulta)

    if len(pesquisa) == 0:
        print('Manifestação não encontrada!')
    else:
        for i in pesquisa:
            print('Código', i[0], '-', i[1], '-', i[4],
                  '-', i[3], '-', 'Descrição:', i[2], '-', 'Data:', i[5])
