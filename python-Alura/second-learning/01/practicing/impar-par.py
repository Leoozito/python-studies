import os
import time

def verificao(numero):
    if numero % 2 == 0:
        os.system('clear')
        print(f"O número {numero} é [Par]")
        continuacao()
    else:
        os.system('clear')
        print(f"O número {numero} é [Impar]")
        continuacao()

def apresentacao_insere_num():
    print("""
    IMPAR OU PAR
--------------------------
""")
    try:
        num_inserido = int(input("Digite o numero: "))
        verificao(num_inserido)
    except ValueError:
        os.system("clear")
        print("Digite apenas números !")
        time.sleep(3)
        os.system('clear')
        main()

def continuacao():
    escolha = str(input("Deseja continuar [S - sim / N - não]\n"))
    if escolha.lower() == 's' or escolha.lower() == 'sim':
        os.system("clear")
        main()
    elif escolha.lower() == 'n' or escolha.lower().replace("ã", "a") == 'nao': 
        os.system('clear')
        print("Saindo do programa...")
        time.sleep(3)
        os.system('clear')
        print("Até breve! 😆")
    else: 
        os.system('clear')
        print("Não compreendi...")
        time.sleep(2)
        continuacao()

def main():
    apresentacao_insere_num()

if __name__ == '__main__':
    main()