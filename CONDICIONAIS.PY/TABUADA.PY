OPERADOR = input('Escolha um operador (+, -, *, /): ')
num1 = int(input('Digite um número: '))

for i in range(1, 11):
    if OPERADOR == '+':
        resultado = num1 + i
        print(f'{num1} + {i} = {resultado}')
    elif OPERADOR == '-':
        resultado = num1 - i
        print(f'{num1} - {i} = {resultado}')
    elif OPERADOR == '*':
        resultado = num1 * i
        print(f'{num1} * {i} = {resultado}')
    elif OPERADOR == '/':
        if i == 0:
            print('Divisão por zero não é permitida.')
        else:
            resultado = num1 / i
            print(f'{num1} / {i} = {resultado}')
    else:
        print('Operador inválido. Por favor, escolha um operador válido (+, -, *, /).')
        break