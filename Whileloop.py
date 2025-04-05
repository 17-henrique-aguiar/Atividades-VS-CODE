# # Questão 1
# loop = 10

# while loop >= 0:
#     print(loop)
#     loop -= 1
# print("Fim da contagem!")

# Questão 2
# loop = 0

# while loop <= 20:     
#     print(loop)
#     loop += 2

# Questão 3 
# numero = 0
# soma = 0

# while numero != -5:
#     numero = int(input(f"Digite um número: "))
#     if numero != -5:
#         soma += numero
# print(f"A soma de todos os números é: {soma}")

# Questão 4
# senha = "cofre2025"
# tentativa = ""

# while tentativa != senha:
#     tentativa = input("Digite o código: ")

# print("Cofre aberto com sucesso!") 

# Questão 5 
import random
while True:
    Jogador_A = random.randint(1,6)
    Jogador_B = random.randint(1,6)

    print(f"Jogador A tirou: {Jogador_A}")
    print(f"Jogador B tirou: {Jogador_B}")

    if Jogador_A > Jogador_B:
        print("Jogador A venceu!")
        break

    print("\n")