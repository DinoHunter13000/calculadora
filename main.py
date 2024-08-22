def soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def dividir(divisor, dividendo):
    return divisor / dividendo

def multiplicar(primeiro_fator, segundo_fator):
    return primeiro_fator * segundo_fator

def executa_calculadora(input_um, input_dois, operacao):
    input_um = input('Digite um valor para a operação Matemática: \n')
    if input_um == 'exit':
        return input_um, input_dois, operacao
    input_um = float(input_um)
    input_dois = input('Digite o segundo valor para a operação Matemática: \n')
    if input_dois == 'exit':
        return input_um, input_dois, operacao
    input_dois = float(input_dois)
    operacao = input(f'Digite o simbolo da operação Matemática para os valores: \n {input_um} \n {input_dois} \n')
    if operacao == 'exit':
        return input_um, input_dois, operacao
    return input_um, input_dois, operacao

saida = ''
input_um = 0
input_dois = 0
operacao = ''

while saida != 'exit':
    (input_um, input_dois, operacao) = executa_calculadora(input_um, input_dois, operacao)

    if input_um == 'exit' or input_dois == 'exit' or operacao  == 'exit':
        saida = 'exit'
    if saida != 'exit':
        resultado = ''
        if operacao == '+':
            resultado = soma(input_um, input_dois)
        elif operacao == '-':
            resultado = subtrair(input_um, input_dois)
        elif operacao == '/':
            resultado = dividir(input_um, input_dois)
        elif operacao == '*':
            resultado = multiplicar(input_um, input_dois)
        else:
            print('Operação não permitida')

        if resultado != '':
            print(f'O resultado da operação {operacao} é: {resultado}')