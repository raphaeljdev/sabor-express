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
3. Ativar restaurante
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
  print(texto)
  print()

def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  restaurantes.append(nome_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
  voltar_ao_menu_principal()


def listar_restaurantes():
  exibir_subtitulo('Listando os restaurantes:')
  for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo}')
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
        print('Ativar restaurante')
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
