print('Olá, Seja Bem-Vindo!')
print('Soma: +\nSubtração: -\nDivisão: /\nMultiplicação: *')
print('---' * 17)
print('Digite "=" no campo operador para obter o resultado')
print('---' * 17)

#Lista que armazena os operandos e operadores
operacao = []

#Funções das quatro operações
def soma(n1, n2):
    total = n1 + n2
    return total

def subtracao(n1, n2):
    total = n1 - n2
    return total

def multiplicacao(n1, n2):
    total = n1 * n2
    return total

def divisao(n1, n2):
    total = n1 / n2
    return total

#Função que deleta os dois operandos e o operador após realizar o calculo
def deletar(index):
    operacao.pop(index)
    operacao.pop(index)
    operacao.pop(index)

#Laço para receber os valores e operadores, adicionar na lista Operacao[], além de tratar excessões e determinar o fim da operação.
while True:
    try:
        operando = int(input('Valor: '))
        operador = input('Operador: ').strip()
        operacao.append(operando)

        if len(operador) == 0:
            print('O campo Operador não pode ficar em branco.')
            
        elif operador == '=':
            break

        operacao.append(operador)
    
    except ValueError:
        print('O campo valor foi inserido com letras ou está em branco')
        
        
#Foi usado um while para as operações de multiplicação e divisão, e outro para soma e subtração, para evitar erro de precedência na operação.
while True:
    if '*' not in operacao and '/' not in operacao:
        break

    #Laço while para fazer o laço for sempre voltar ao início após passar por alguma condição, para não ter erro de precedência na operação.
    while True:
        if '*' not in operacao and '/' not in operacao:
            break

        for idx, i in enumerate(operacao):

            if i == '/':
                valor_1 = operacao[idx - 1]
                valor_2 = operacao[idx + 1]
                dividido = divisao(valor_1, valor_2)
                deletar(idx - 1)
                operacao.insert(idx - 1, dividido)
                break

            elif i == '*':
                valor_1 = operacao[idx - 1]
                valor_2 = operacao[idx + 1]
                multiplicado = multiplicacao(valor_1, valor_2)
                deletar(idx - 1)
                operacao.insert(idx - 1, multiplicado)
                break


while True:
    if '+' not in operacao and '-' not in operacao:
        break
    
    #Laço while para fazer o laço for sempre voltar ao início após passar por alguma condição, para não ter erro de precedência na operação.
    while True:
        if '+' not in operacao and '-' not in operacao:
            break
    
        for idx, i in enumerate(operacao):
            
            if i == '+':
                valor_1 = operacao[idx - 1]
                valor_2 = operacao[idx + 1]
                somado = soma(valor_1, valor_2)

                deletar(idx - 1)
                operacao.insert(idx - 1, somado)
                break

            elif i == '-':
                valor_1 = operacao[idx - 1]
                valor_2 = operacao[idx + 1]
                subtraido = subtracao(valor_1, valor_2)

                deletar(idx - 1)
                operacao.insert(idx - 1, subtraido)
                break

valor = round(operacao[0], 3)
print(f'Resultado: {valor}')