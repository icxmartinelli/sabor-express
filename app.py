import os

# OBS GERAIS SOBRE O PYTHON
# não tem problema usar aspas simples ou duplas
# aspas duplas serve para preservar as quebras de linhas
# if / elif / else

restaurantes = [{'id':0, 'nome':'default','ativo':False}]
# iniciamos o dictionary apenas para testes

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair do app')

def encerrar_app():
    exibir_subtitulo('encerrar', True)

def reiniciar():
    if input_sim_nao('deseja reiniciar'):
        main()
    else:
        if input_sim_nao('deseja finalizar'):
            encerrar_app()
        else:
            reiniciar()

def opcao_invalida():
    print('opção inválida')
    reiniciar()

def exibir_subtitulo(subtitulo, limpar_tela):
    if limpar_tela: os.system('cls')
    linha = '-' * 100
    # quantidade de espaços para permitir o texto ficar centralizado
    centralizar = ' ' * int((100 - len(subtitulo)) / 2)
    print(linha)
    print(centralizar, subtitulo, centralizar)
    print(linha)

def input_sim_nao(pergunta):
    resposta = ''
    print('-' * 100)
    # repetimos a pergunta até obtermos uma resposta válida
    while resposta not in ['s', 'n']: resposta = input(f'{pergunta}? s / n ').lower()
    if resposta == 's' :
        return True
    else:
        return False

def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes', True)
    # recebemos o nome
    nome_restaurante = input('nome: ')
    # adicionamos novo dictionary à lista
    restaurantes.append({'id':len(restaurantes),'nome':nome_restaurante,'ativo':False})
    # informamos o sucesso do cadastro
    print(f'restaurante', nome_restaurante, 'cadastrado com sucesso')
    if input_sim_nao('deseja cadastrar novo restaurante'):
        cadastrar_novo_restaurante()
    else:
        listar_restaurante(True)

def listar_restaurante(limpar_tela_):
    exibir_subtitulo('lista de restaurantes', limpar_tela_)
    # 10 | 80 | 10 -> espaços reservados para cada campo
    for restaurante in restaurantes:
        print(' | '.join(f'{key}: {value if not isinstance(value, bool) else ('sim' if value else 'não')}'.ljust(74 if key == 'nome' else 10) for key, value in restaurante.items()))
    if limpar_tela_: reiniciar()

def alterar_ativo_restaurante(limpar_tela):
    try:

        if (limpar_tela) : os.system('cls')
        
        id_ = ''
        encontrou = False

        # exibimos uma lista dos restaurantes cadastrados antes de ativar ou inativar
        listar_restaurante(False)
        exibir_subtitulo('alterar ativo do restaurante', False)

        # repetimos a pergunta até obtermos uma resposta válida
        while not id_.isdigit(): id_ = input('digite o id: ')
        
        for restaurante in restaurantes:
            if int(id_) == restaurante['id']:
                encontrou = True
                print(f'o restaurante', restaurante['nome'], 'está', 'ativo' if restaurante['ativo'] else 'inativo')
                # se o usuário desejar alterar o status, alteramos
                if input_sim_nao(f'deseja {'ativar' if not restaurante['ativo'] else 'inativar'}'): restaurante['ativo'] = not restaurante['ativo']
                # de todo modo, listamos novamente
                listar_restaurante(True)
        
        if not encontrou:
            exibir_subtitulo(f'restaurante de id {id_} não encontrado', True)
            alterar_ativo_restaurante(False)

    except:
        opcao_invalida()

def escolher_opcao():
    try:
        opcao_escolhida = ''
        # repetimos a pergunta até obtermos uma resposta válida
        while not opcao_escolhida.isdigit(): opcao_escolhida = input('escolha uma opção de 1 a 4: ')
        match int(opcao_escolhida):
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurante(True)
            case 3:
                 alterar_ativo_restaurante(True)
            case 4:
                encerrar_app()
            case _: # case else aqui
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_subtitulo('sabor express', True)
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()