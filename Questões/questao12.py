import random 

#Criando uma list Comprehession
lista = [random.randint(1, 50) for _ in range(10)]

valor = int(input("Digite um valor a ser encontrado na lista: "))

if valor in lista:
  print("O valor está na lista")
else:
  print("O valor não está na lista")