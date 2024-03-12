def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        i = 2
        while i < n:
            next_number = sequence[i-1] + sequence[i-2]
            sequence = sequence + [next_number]
            i += 1
        return sequence


def verifica_pertence(numero):
    sequence = fibonacci(numero)
    if numero in sequence:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


numero = int(input("Digite um número: "))
resultado = verifica_pertence(numero)
print(resultado)
