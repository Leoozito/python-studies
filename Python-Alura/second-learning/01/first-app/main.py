import os
import time 

def apresentation_of_program():
    print("""
    SEJA BEM VINDO AO -

    █▀▀ █░█ █░░ █░░   ▀█▀ █░█ █▀▄▀█ █▀▄▀█ █▄█
    █▀░ █▄█ █▄▄ █▄▄   ░█░ █▄█ █░▀░█ █░▀░█ ░█░   
               
""")
    
def apresentation_of_options():
    print("""
    ---------------------------------------------
    Opções:

    [ 1 ] - Cadastrar restaurante
    [ 2 ] - Listar restaurantes
    [ 3 ] - Ativar restaurante
    [ 4 ] - Sair do Programa 
    ---------------------------------------------    
""")
    
def choose_option():
    chosen_option = int(input("Digite o n° da opção desejada: "))
    
    if chosen_option == 1:
        register_restaurant()
    elif chosen_option == 2:
        list_restaurant()
    elif chosen_option == 3:
        activate_restaurant()
    elif chosen_option == 4:
        exit_program()
    else:
        os.system("clear") 
        print("Opção invalida !  ✘")
        time.sleep(3)
        apresentation_of_options()

def register_restaurant():
    print("Cadastrar restaurante")

def list_restaurant():
    print("Restaurantes")

def activate_restaurant(): 
    print("Ativar restaurante")

def exit_program():
    os.system('clear')
    # os.system('cls') para macIOS
    print("Saindo do programa...")
    time.sleep(3)
    os.system('clear')
    print("Até breve! 😆")

def main():
    apresentation_of_program()
    apresentation_of_options()
    choose_option()

if __name__ == '__main__':
    main()