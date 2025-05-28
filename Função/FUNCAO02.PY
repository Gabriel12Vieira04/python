def divisao_e_resto(a, b):
    """Retorna o quociente e i resto da divisão de a por b."""
    quociente = a // b
    resto = a % b
    return quociente, resto

resultado = divisao_e_resto(10, 3)
print(f"Quociente: {resultado[0]}, Resto: {resultado[1]}")
# Saída esperada:   Quociente: 3, Resto: 1
# Função que calcula o quociente e o resto da divisão de dois números       