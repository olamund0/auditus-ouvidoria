from classe import *


def alterarmanifestacao(conexao):
    consulta = 'select count(*) from manifestacao'
    manifestacao = listarBancoDados(conexao, consulta)
    quantidade = manifestacao[0][0]

    if quantidade == 0:
        print('Não existem manifestações cadastradas!')
    else:
        listar = 'select * from manifestacao'
        manifestacao = listarBancoDados(conexao, listar)
        for i in manifestacao:
            print('Código', i[0], '-', i[1], '-', i[4], '-', i[3])

        codigo = input(
            'Informe o código da manifestação que deseja alterar o título e descrição \nDigite: ')
        consulta = 'select * from manifestacao where codigo = ' + codigo
        resultado = listarBancoDados(conexao, consulta)

        if len(resultado) == 0:
            print('Manifestação não encontrada!')
        else:
            novoTitulo = input('Digite o novo título: ')
            novaDescricao = input('Digite a nova descrição: ')
            sqlAtualizar = 'update manifestacao set titulo = %s, descricao = %s  where codigo = %s '
            valores = [novoTitulo, novaDescricao, codigo]
            atualizarBancoDados(conexao, sqlAtualizar, valores)
            print('Manifestação editada com sucesso!')
