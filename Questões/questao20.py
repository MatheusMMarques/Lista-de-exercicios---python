numeros = []
contador = 0

while contador < 10:
    numero = int(input("Digite um numero impar: "))
    if numero % 2 != 0:
      numeros.append(numero)
      contador += 1
    else:
        print("O número digitado não é impar, tente novamente.")


print("Os números digitados são: ")
for numero in numeros:
  print(numero)