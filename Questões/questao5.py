idade = int(input("Digite sua idade: "))

print ("Sua idade é:",idade)

if idade <= 11:
  print("Você é Criança.")
elif idade >= 12 and idade <= 18:
  print("Você é Adolecente.")
elif idade >= 19 and idade <= 24:
  print("Você é Jovem.")
elif idade >= 25 and idade <= 40:
  print("Você é Adulto.")
elif idade >= 41 and idade <=60:
  print("Você está na meia idade.")
else:
  print("Você é uma pessoa idosa.")
