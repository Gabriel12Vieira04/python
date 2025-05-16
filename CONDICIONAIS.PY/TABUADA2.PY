opcoes = 0
while opcoes != 5:
    print('ESCOLHA UMA OPÇÃO')
    print("(1) Somar")
    print('(2) Diminuir')
    print('(3) Multiplicação')
    print('(4) Divisão')
    print('(5) Sair')
    opcoes = int(input('=> '))
    if opcoes in [1, 2, 3, 4]:
        num1 = int(input("Digite um numero? "))
        for i in range(1, 11):
            if opcoes == 1:
                resultado = num1 + i
                print(f'{num1} + {i} = {resultado}')
            elif opcoes == 2:
                resultado = num1 - i
                print(f'{num1} - {i} = {resultado}')
            elif opcoes == 3:
                resultado = num1 * i
                print(f'{num1} * {i} = {resultado}')
            elif opcoes == 4:
                if i == 0:
                    print('Divisão por zero não é permitida.')
                else:
                    resultado = num1 / i
                    print(f'{num1} / {i} = {resultado}')
            else:
                print('Operador inválido. Por favor, escolha um operador válido (+, -, *, /).')
                break