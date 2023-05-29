opcao = 0

while opcao not in [1, 2, 3]:
    print("MENU DE OPÇÕES:")
    print("1 - Olá mundo")
    print("2 - Eu programo em Python")
    print("3 - Laços de repetição")
    opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    print("Olá mundo!")
elif opcao == 2:
    print("Eu programo em Python!")
elif opcao == 3:
    print("Laços de repetição são muito úteis na programação!")

