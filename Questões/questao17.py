numeros = []

for _ in range(10):
  numero = int(input("Digite um número: "))
  numeros.append(numero)

for i in range(len(numeros)):
  if numeros[i] % 2 == 0:
    numeros[i] += 1

print("Os números digitados são: ")

for numero in numeros:
  print(numero)