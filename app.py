import os

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

def opcao_invalida():
  print('Condicao invalida\n')
  input('Digite uma tecla para voltar ao menu principal\n')
  main()
  
def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opcao: '))
    match opcao_escolhida:
      case 1:
        print('Cadastrar restaurante')
      case 2:
        print('Listar restaurante')
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