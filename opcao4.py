from classe import *


def quantidademanifestacao(conexao):
    consulta = 'select count(*) from manifestacao'
    manifestacao = listarBancoDados(conexao, consulta)
    quantidade = manifestacao[0][0]
    print('Quantidade de manifestações:', quantidade)

    elogio = 'select count(*) from manifestacao where tipo = "Elogio"'
    manifestacao = listarBancoDados(conexao, elogio)
    quantidade = manifestacao[0][0]
    print('Quantidade de Elogios:', quantidade)

    reclamacao = 'select count(*) from manifestacao where tipo = "Reclamação"'
    manifestacao = listarBancoDados(conexao, reclamacao)
    quantidade = manifestacao[0][0]
    print('Quantidade de Reclamações', quantidade)

    sugestao = 'select count(*) from manifestacao where tipo = "Sugestão"'
    manifestacao = listarBancoDados(conexao, sugestao)
    quantidade = manifestacao[0][0]
    print('Quantidade de Sugestões', quantidade)
