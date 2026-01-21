import os

restaurantes  = ['Picanha', 'Maminha']

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
  os.system('clear')
  print('Programa finalizado.')

def voltar_ao_menu_principal():
  input('\nDigite uma tecla para voltar ao menu principal\n')
  main()

def opcao_invalida():
  print('Condicao invalida\n')
  voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
  os.system('clear')
  print('Cadastro de novos restaurantes\n')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  restaurantes.append(nome_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
  voltar_ao_menu_principal()


def listar_restaurantes():
  os.system('clear')
  print('Listando os restaurantes:\n')
  for restaurante in restaurantes:
    print(f'.{restaurante}')
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