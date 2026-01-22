import os

restaurantes  = [
    {'nome':'Praca', 'categoria':'Japonesa', 'ativo':False}, 
    {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},     
    {'nome':'Cantina', 'categoria':'Brasileira', 'ativo':False}, 
]

def exibir_nome_do_programa():
  mensagem_inicial = """

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
"""
  print(mensagem_inicial)

def exibir_opcoes():
  print("""
1. Cadastrar restaurante
2. Listar restaurante
3. Alternar estado do restaurante
4. Sair
""")
  
def finalizar_programa():
  exibir_subtitulo('Programa finalizado.')

def voltar_ao_menu_principal():
  input('\nDigite uma tecla para voltar ao menu principal\n')
  main()

def opcao_invalida():
  print('Condicao invalida\n')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
  os.system('clear')
  linha = '*' * (len(texto))
  print(linha)
  print(texto)
  print(linha)
  print()

def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
  dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
  voltar_ao_menu_principal()


def listar_restaurantes():
  exibir_subtitulo('Listando os restaurantes:')

  print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
  for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
  voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado.')

    voltar_ao_menu_principal()
  
def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opcao: '))
    match opcao_escolhida:
      case 1:
        cadastrar_novo_restaurante()
      case 2:
        listar_restaurantes()
      case 3:
        alternar_estado_restaurante()
      case 4:
        finalizar_programa()   
      case _:
        opcao_invalida()   
  except:
    opcao_invalida()
  
def main():
  os.system('clear')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()

if __name__ == '__main__':
  main()
