from classe import *


def excluirmanifestacao(conexao):
    consulta = 'select count(*) from manifestacao'
    manifestacao = listarBancoDados(conexao, consulta)
    quantidade = manifestacao[0][0]

    if quantidade == 0:
        print('Não existem manifestações cadastradas!')
    else:

        excluir = int(input(
            'O que deseja? \n1)Excluir manifestação por código \n2)Excluir todas manifestações \nDigite: '))

        if excluir == 1:

            listar = 'select * from manifestacao'
            manifestacao = listarBancoDados(conexao, listar)
            for i in manifestacao:
                print('Código', i[0], '-', i[1], '-', i[4], '-', i[3])

            codigo = input(
                'Digite o código da manifestação que deseja excluir: ')
            consulta = 'select * from manifestacao where codigo = ' + codigo
            resultado = listarBancoDados(conexao, consulta)

            if len(resultado) == 0:
                print('Manifestação não encontrada!')
            else:
                remover = 'delete from manifestacao where codigo = %s '
                dados = [codigo]
                excluirBancoDados(conexao, remover, dados)
                print('Manifestação excluída com sucesso!')

        elif excluir == 2:

            codigo = 0
            remover = 'delete from manifestacao where codigo > %s'
            dados = [codigo]
            excluirBancoDados(conexao, remover, dados)
            print('Manifestações excluídas com sucesso!')

        else:
            print('Opção inválida!')
