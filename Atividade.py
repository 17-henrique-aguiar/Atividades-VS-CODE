# QUESTÃO 1

# pague = str(input("Insira seu método de pagamento: "))

# if pague == "cartao":
#     print("Processando pagamento no cartão...")
# elif pague == "boleto":
#     print("Gerando boleto bancário...")
# else:
#     print("Método de pagamento não reconhecido.")

# QUESTÃO 2 ---------------------

# idade = int(input("Digite sua idade: "))

# if idade <= 12:
#     print ("Criança")
# elif idade >= 13 and idade <= 17:
#     print("Adolescente")
# elif idade >= 18 and idade <= 59:
#     print("Adulto")
# elif idade >= 60:
#     print("Idoso")

# QUESTÃO 3 ----------------------

# valor_compra = float(input("Insiro o valor da sua compra: "))

# des10 = 200.00
# des15 = 300.00
# des20 = 400.00

# if valor_compra >= des10 and valor_compra < des15:
#     valor_comdes = valor_compra * 0.10
# elif valor_compra >= des15 and valor_compra < des20:
#     valor_comdes = valor_compra * 0.15
# elif valor_compra >= des20:
#     valor_comdes = valor_compra * 0.20
# else:
#     valor_comdes = 0

# print(f"Valor do desconto: R$ {valor_comdes}")

# QUESTÃO 4 -------------------------

# entrega = str(input("Qual seu tipo de entrega: "))

# if entrega == "padrão":
#     print("Custa R$ 10,00")
# elif entrega == "expresso":
#     print("Custa R$ 20,00")
# else:
#     print("Opção de entrega inválida.")

# QUESTÃO 5 ----------------------------

# nota = int(input("insira sua nota(de 0 a 100): "))

# if nota < 50:
#     print("Reprovado!")
# elif nota >= 50 and nota <= 69:
#     print("Recuperação!")
# elif nota >= 70 and nota <= 89:
#     print("Aprovado!")
# elif nota >= 90:
#     print("Aprovado com exelência!")

# QUESTÃO 6 ----------------------------

tempo_permanencia = float(input("Insira o tempo de permanência(em horas): "))

if tempo_permanencia <= 1:
    print("Valor a ser pago: R$ 5,00")
elif tempo_permanencia > 1 and tempo_permanencia <= 3:
    print("Valor a ser pago: R$ 10,00")
elif tempo_permanencia > 3 and tempo_permanencia <= 6:
    print("Valor a ser pago: R$ 15,00")
elif tempo_permanencia > 6:
    print("Valor a ser pago: R$ 25,00")
