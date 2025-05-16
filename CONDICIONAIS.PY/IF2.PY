nome = input('Qual seu nome? ')
idade = int(input("Qual a sua idade? "))
peso = float(input('Qual o seu peso?'))


if idade <= 17:
    print('menor')

elif idade >= 18 and idade <=59:
    print('maior')

else:
    print('idoso')
