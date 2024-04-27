import os 
import time

email_definido = 'leonardo@gmail.com'
senha_definido = '123'

def apresentacao():
    os.system("clear")
    print("""
    -------------------------------------          
               - BEAR SHOP - 
        Vendas de bebidas alcoolicas
    -------------------------------------
              SEJA BEM VINDO
          """)

def verifica_user():
    tentativas = 0

    print("Nos informe seu email e senha")
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    
    if email == email_definido and senha == senha_definido:
        verifica_idade()
    else:
        tentativas += 1
        os.system("clear")
        print("Email ou Senha incorreto\n\n")
        if tentativas > 3:
            print("Infelizmente excedeu o número de tentativas. Tente novamente mais tarde")
        else:
            verifica_user()

def verifica_idade():
    try:
        idade = int(input("Informe sua idade: "))
        if idade >= 18:
            apresentacao()
        else:
            print("""
            -----------------------------------------------------------------------
                Infelizmente você ainda não pode comprar de nossos produtos.
                Esperamos você talvez em breve, compartilhe nossa shop de bebidas
            -----------------------------------------------------------------------
            """)
    except ValueError:
        os.system("clear")
        print("Digite apenas números !")
        time.sleep(3)
        os.system('clear')
        main()


def main():
    verifica_user()

if __name__ == '__main__':
    main()
