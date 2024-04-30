import os

users_registered = [{'nome':'Leonardo', 'idade':'21 anos', 'cidade':'São Paulo'}]

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
    apresentation("Dados do Usuário")
    print(f'{"NOME".ljust(20)} {"IDADE".ljust(20)} {"CIDADE"}')
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

def apresentation(text):
    os.system('clear')
    print("=-" * len(text))
    print(f"""          {text.upper()}\n""")

def update_name(user):
    apresentation("Editar NOME do usuário")
    new_name = str(input("Digite novo nome desejado: "))
    confirm_update_datas('nome', new_name, user['nome'])

def update_years(user):
    apresentation("Editar IDADE do usuário")
    new_year = str(input("Digite nova idade: "))
    confirm_update_datas('idade', new_year, user['idade'])

def update_city(user):
    apresentation("Editar CIDADE do usuário")
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