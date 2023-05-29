#Introduzindo as notas
port = float(input("Digite sua nota de português: "))
ing = float(input("digite sua nota de inglês: "))
mtm = float(input("digite sua nota de matemática: "))

#calculando Média
media = (port + ing + mtm)/3

if media >= 7:
  print("Aluno Aprovado")
else:
  print("Aluno Reprovado")

