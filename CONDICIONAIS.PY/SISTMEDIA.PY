aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média do aluno {aluno} é: {media:.2f}")   

if media >= 7: 
    print(f"O aluno {aluno} está aprovado.")
elif media >= 5 and media < 7:
    # A média é maior ou igual a 5 e menor que 7
    print(f"O aluno {aluno} está em recuperação.")
else:
    print(f"O aluno {aluno} está reprovado.")