def convertendoHex (converter):
    conversao = int(converter,16)
    return conversao

def convertendoOct (converter):
    conversao = int(converter,8)
    return conversao

def convertendoBin (converter):
    conversao = int(converter,2)
    return conversao


print("PROGRAMMER PARIZOTO")

print("Bem-vindo programa Sistemas-Ciber Fisicos")

print(''' Escolha sua opção: 
1 - NUMERO PARA BIN, OCT E HEX.
2 - BIN, OCT E HEX PARA NUMERO.
''')
opcao = int(input("Digite qual opção deseja usar: "))
while opcao < 1 or opcao > 2:
    print("A opção que digitou não existe tente novamente.")
    opcao = int(input("Digite uma opcao valida: "))


if opcao == 1:
    numero = int(input("Digite o numero desejado: "))

    print('''Para qual valor deseja fazer a conversão?
1 - BINÁRIA
2 - OCTADECIMAL
3 - HEXADECIMAL''')

    escolha = int(input("Digite a sua escolha: "))
    while escolha < 1 or escolha > 3:
        print("A escolha que digitou não existe tente novamente.")
        escolha = int(input("Digite uma escolha valida: "))

    if escolha == 1:
        print("O numero {} foi convertido para BINARIO: {}".format(numero,bin(numero)[2:]))
    elif escolha == 2:
        print("O numero {} foi convertido para OCTADECIMAL:{}".format(numero,oct(numero)[2:]))
    elif escolha == 3:
        print("O numero {} foi convertido para HEXADECIMAL: {}".format(numero,hex(numero)[2:]))

elif opcao == 2:
    print('''
Escolha a opção desejada:
1 - BINARIA para decimal.
2 - OCTADECIMAL para decimal.
3 - HEXADECIMAL para decimal.
    ''')

    opcao = int(input("Digite a expressão desejada: "))
    while opcao < 1 or opcao > 3:
        print("A opção que digitou não existe tente novamente.")
        opcao = int(input("Digite uma opcao valida: "))

    if opcao == 1:
        string = input("Digite qual deseja converter:")
        converter = string

        print("{} foi convertido para Binario: {}".format(string, convertendoBin(converter)))

    elif opcao == 2:
        string = input("Digite qual deseja converter:")
        converter = string

        print("{} foi convertido para OCTADECIMAL: {}".format(string, convertendoOct(converter)))

    elif opcao == 3:
        string = input("Digite qual deseja converter:" )
        converter = string

        print("{} foi convertido para HEXADECIMAL: {}".format(string, convertendoHex(converter)))

