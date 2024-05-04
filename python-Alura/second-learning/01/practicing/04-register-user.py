import os
import time

users_registered = [{'nome':'Leonardo', 'idade':'21 anos', 'cidade':'São Paulo'}]

def menu_options():
    apresentation_tile("Sistema de Usuario")
    
    try:
        choice = int(input("""
            Tecle:
            [ 1 ] Cadastro de novo usuario 
            [ 2 ] Editar novo usuario
            [ 3 ] Listar usuarios

        """))
        if choice == 1:
            post_user()
        elif choice == 2:
            update_user()
        elif choice == 3:
            list_user()
        else:
            print("Opção invalida, tecle um número referente as opções")
            time.sleep(3)
            menu_options()
    expect NameError:
        os.system("clear")
        print("Digite apenas números !")
        time.sleep(3)
        os.system('clear')
        menu_options()

def post_user():
    pass

def update_user():
    pass
    
def list_user():
    pass

def update_register_user():
    user_insert = str(input("Digite o nome do usuário: "))
    
    user_found = False
    for user in users_registered:
        if user['nome'] == user_insert:
            user_found = not user_found
            menu_update(user)
    if not user_found:
        print("Usuario não encontrado")

def menu_update(user):
    apresentation_title("Dados do Usuário")
    print(f'{"NOME".ljust(22)} {"IDADE".ljust(22)} {"CIDADE"}')
    print(f"{user['nome'].ljust(20)} | {user['idade'].ljust(20)} | {user['cidade']}")
    choice = int(input("""
        O que gostaria de editar?
                
        [1] Nome
        [2] Idade
        [3] Cidade
    """))

    if choice == 1:
        update_name(user)
    elif choice == 2:
        update_years(user)
    elif choice == 3:
        update_city(user)
    else:
        os.system('clear')
        print("Opção invalida\n")
        menu_update()

def apresentation_title(text):
    os.system('clear')
    print("=-" * len(text))
    print(f"""          {text.upper()}\n""")

def update_name(user):
    apresentation_title("Editar NOME do usuário")
    new_name = str(input("Digite novo nome desejado: "))
    confirm_update_datas('nome', new_name, user['nome'])

def update_years(user):
    apresentation_title("Editar IDADE do usuário")
    new_year = int(input("Digite nova idade: "))
    confirm_update_datas('idade', new_year, user['idade'])

def update_city(user):
    apresentation_title("Editar CIDADE do usuário")
    new_city = str(input("Digite a nova cidade: "))
    confirm_update_datas('idade', new_city, user['cidade'])

def confirm_update_datas(data_update, data_new, data_older):
    resp_confirm = str(input(f"Confirma a modificação do {data_update.upper()} do Usuario: {data_older} para {data_new}? [S/N]")) if data_new else str(input(f"Insira um(a) novo(a) {data_update.upper()}"))

    if resp_confirm.lower() == "s":
        os.system("clear")
        print(f"{data_update.upper()} do usuario editado com sucesso !")
        data_older = data_update

    elif resp_confirm.lower() == "n":
        input("Clique qualquer tecla para voltar ao menu inicial") 
        main()
    else:
        print(f"""Não compreendi, digite "s" para "SIM" ou "n" para "NÃO" , tente novamente...""")
        confirm_update_datas()


def registered_user():
    pass

def main():
    update_register_user()

if __name__ == '__main__':
    main()