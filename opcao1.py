from classe import *


def listartudo(conexao):
    consulta = 'select count(*) from manifestacao'
    manifestacao = listarBancoDados(conexao, consulta)
    quantidade = manifestacao[0][0]

    if quantidade == 0:
        print('Não existem manifestações cadastradas!')
    else:
        listar = 'select * from manifestacao'
        manifestacao = listarBancoDados(conexao, listar)
        for i in manifestacao:
            print('Código', i[0], '-', i[1], '-',
                  i[4], '-', i[3], '-', 'Data:', i[5])
