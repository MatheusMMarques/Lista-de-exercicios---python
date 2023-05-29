numeros = list(range(1, 11))  # Cria a lista com valores de 1 a 10
indice = 0

while indice < len(numeros):
    if numeros[indice] % 2 == 0:
      print(numeros[indice])
    indice += 1