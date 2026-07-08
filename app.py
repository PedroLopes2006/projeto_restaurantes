import os
import subprocess


restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]


def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_subtitulo(texto):
    subprocess.run(["cls"], shell=True)
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')


def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu_principal()


def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida():
    print('Opção Invalida\n')
    voltar_menu_principal()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    voltar_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes:')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        def opcao(opcao_escolhida):
            match opcao_escolhida:
                case 1:
                    cadastrar_novo_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    return 'Ativar Restaurante'
                case 4:
                    subprocess.run(["cls"], shell=True)
                    return 'Programa Finalizado'
                case _:
                    opcao_invalida()

        print(opcao(opcao_escolhida))
    except:
        opcao_invalida()


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
