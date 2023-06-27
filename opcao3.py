from classe import *


def criarmanifestacao(conexao):
    classe = int(input('Qual manifestação deseja criar?'
                       '\n1)Elogio \n2)Reclamação \n3)Sugestão \nDigite: '))
    if classe == 1:
        tipo = 'Elogio'

    elif classe == 2:
        tipo = 'Reclamação'

    elif classe == 3:
        tipo = 'Sugestão'

    else:
        tipo = 'Outros'

    autor = input('Digite seu nome: ')
    titulo = input('Dê um título para sua manifestação: ')
    descricao = input('Descreva sua manifestação: ')
    data = str(input('Digite o dia em que o fato ocorreu (formato DD/MM/AA): '))
    sqlInsercao = 'insert into manifestacao (titulo,descricao,autor,tipo,data) values(%s,%s,%s,%s,%s)'
    valores = [titulo, descricao, autor, tipo, data]
    insertNoBancoDados(conexao, sqlInsercao, valores)
    print('Manifestação cadastrada com sucesso!')
