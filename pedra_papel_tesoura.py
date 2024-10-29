from random import choice
from time import sleep

pergunta = str(input("Deseja jogar pedra, paapel ou tessoura com o computador? (sim/não) ").strip().lower())
lista = ["pedra", "papel", "tesoura"]

while pergunta not in "naoo nãoo":
    if pergunta in "simm":

        
        

        print("\n\033[1;34mO computador está escolhendo...\033[m\n")
        escolhaC = choice(lista)
        sleep(5)
        
        print("\n\033[1;34mPronto! pense um pouco na sua escolha também...\033[m")
        while True:
            escolha = str(input("faça sua escolha (pedra, papel ou tessoura): ").strip().lower())
            if escolha == "pedra" or escolha == "papel" or escolha == "tesoura":
                break
            else:
                print("\n\033[1;31mResposta inválida!\033[m\n")

        print("\n\033[1;34mVamos ver quem venceu...\033[m")
        sleep(2)

        if escolha == escolhaC:
            print(f"\n\033[1;33mVocê e o computador escolheram\033[m {escolha}\033[1;33m! Ninguém venceu ksk\033[m")
        elif escolha == "pedra" and escolhaC == "papel":
            print(f"\033[1;31mO computador escolheu\033[m {escolhaC}\033[1;31m! Você PERDEU!\033[m")
        elif escolha == "pedra" and escolhaC == "tesoura":
            print(f"\033[1;32mO computador escolheu\033[m {escolhaC}\033[1;32m! Você VENCEU!\033[m")
        elif escolha == "papel" and escolhaC == "pedra":
            print(f"\033[1;32mO computador escolheu\033[m {escolhaC}\033[1;32m! Você VENCEU!\033[m")
        elif escolha == "papel" and escolhaC == "tesoura":
            print(f"\033[1;31mO computador escolheu\033[m {escolhaC}\033[1;31m! Você PERDEU!\033[m")
        elif escolha == "tesoura" and escolhaC == "pedra":
            print(f"\033[1;31mO computador escolheu\033[m {escolhaC}\033[1;31m! Você PERDEU!\033[m")
        else:
            print(f"\033[1;32mO computador escolheu\033[m {escolhaC}\033[1;32m! Você VENCEU!\033[m")

    else:
        print("\n\033[1;31mVocê precisa digitar sim ou não!\033[m\n")

    print(100 * "-")
    pergunta = str(input("Deseja jogar pedra, papel ou tessoura com o computador? (sim/não) ").strip().lower())

print("Programa finalizado!")

