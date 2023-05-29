#Criando lista vazia
lista = []

name1 = str(input("digite um nome: "))
lista.append(name1) #Adicionando nomes na lista vazia
print(lista)

name2 = str(input("digite um segundo nome: "))
lista.append(name2) #Adicionando nomes na lista vazia
print(lista)

name3 = str(input("digite um terceiro nome: "))
lista.append(name3) #Adicionando nomes na lista vazia
print(lista)

name4 = str(input("digite um quarto nome: "))
lista.append(name4) #Adicionando nomes na lista vazia
print(lista)

name5 = str(input("digite um quinto nome: "))
lista.append(name5) #Adicionando nomes na lista vazia
print(lista)

name_removido = int(input("Digite um numero de 0 a 4: "))

#Criando condições de remoção para cada numero que o usuário pode escolher
if name_removido == 0:
  lista.remove(name1)
elif name_removido == 1:
  lista.remove(name2)
elif name_removido == 2:
  lista.remove(name3)
elif name_removido == 3:
  lista.remove(name4)
else:
  lista.remove(name5)
  print(lista)
