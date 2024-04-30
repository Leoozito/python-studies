import os
import time 

all_restaurants = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Italiano', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

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

    try:        
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
    except NameError:
        os.system("clear")
        print("Digite apenas números !")
        time.sleep(3)
        os.system('clear')
        main()

def register_restaurant():
    subtitle_topics('Cadastrar restaurantes')

    name_restaurant = str(input("Digite o nome do restaurante: "))
    category_restaurant = str(input(f"Digite a categoria do restaurante {name_restaurant}")) 

    data_restaurant = {'nome': name_restaurant,'categoria': category_restaurant, 'ativo': False}
    all_restaurants.append(data_restaurant)
    os.system('clear')
    print(f"Restaurante {name_restaurant} cadastrado com sucesso !!")
    
    back_to_menu()

def list_restaurant():
    subtitle_topics("Restaurantes cadastrados")

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurants in all_restaurants:
        name_restaurants = restaurants['nome']
        category = restaurants['categoria']
        status = restaurants['ativo']
        print(f'-   {name_restaurants.ljust(20)} | {category.ljust(20)} | {status}')

    back_to_menu()

def activate_restaurant(): 
    subtitle_topics("Ativar/Desativar restaurante")
    
    name_restaurant = str(input("Digite o nome do restaurante que deseja acessar"))
    found_restaurant = False 
    for restaurants in all_restaurants:
        if name_restaurant == restaurants['nome']:
            found_restaurant = True
            restaurants['ativo'] = not restaurants['ativo']
            mensagem = f'O {name_restaurant} foi ativado com sucesso' if restaurants['ativo'] else f'O {name_restaurant} foi desativado com sucesso'
            print(mensagem)

    if not found_restaurant:
        print(f"Restaurante {name_restaurant} não encontrado !")

    back_to_menu()

def exit_program():
    os.system('clear')
    # os.system('cls') para macIOS
    print("Saindo do programa...")
    time.sleep(3)
    os.system('clear')
    print("Até breve! 😆")

def subtitle_topics(name_of_topic):
    os.system('clear')
    print("=-" * len(name_of_topic))
    print(f"""          {name_of_topic.upper()}\n""")

def back_to_menu():
    input("\nClique qualquer tecla para voltar ao menu principal !")
    main()

def main():
    apresentation_of_program()
    apresentation_of_options()
    choose_option()

if __name__ == '__main__':
    main()