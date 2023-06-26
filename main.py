from classe import *
from opcao1 import *
from opcao2 import *
from opcao3 import *
from opcao4 import *
from opcao5 import *
from opcao6 import *
from opcao7 import *

opcao = 1

conexao = abrirBancoDados('localhost', 'user', 'password', 'ouvidoria')


def sair():
    print('Saiu')


def opcaoinvalida():
    print('Opção inválida!')


print('-------------Seja Bem-vindo(a)-------------')

while opcao != 8:
    print()
    print('1)Listar todas manifestações\n')
    print('2)Listar manifestações por tipo\n')
    print('3)Criar nova manifestação\n')
    print('4)Exibir quantidade de manifestações\n')
    print('5)Pesquisar manifestação por código\n')
    print('6)Alterar o Título e Descrição de uma manifestação\n')
    print('7)Excluir uma manifestação por código\n')
    print('8)Sair do sistema\n')
    print()

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        listartudo(conexao)

    elif opcao == 2:
        listarportipo(conexao)

    elif opcao == 3:
        criarmanifestacao(conexao)

    elif opcao == 4:
        quantidademanifestacao(conexao)

    elif opcao == 5:
        pesquisarcodigo(conexao)

    elif opcao == 6:
        alterarmanifestacao(conexao)

    elif opcao == 7:
        excluirmanifestacao(conexao)

    elif opcao == 8:
        sair()

    else:
        opcaoinvalida()


encerrarBancoDados(conexao)


print('Obrigado por usar nosso sistema!')
