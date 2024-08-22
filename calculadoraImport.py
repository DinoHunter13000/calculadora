from operacoes import soma, subtrair, dividir, multiplicar

def recebe_numero():
    input_var = input('Digite um valor para a operação Matemática: \n')
    input_var = float(input_var) if input_var != 'exit' else input_var
    return input_var

def executa_calculadora(input_um, input_dois, operacao):
    input_um = recebe_numero()
    if input_um == 'exit':
        return input_um, input_dois, operacao
    input_dois = recebe_numero()
    if input_dois == 'exit':
        return input_um, input_dois, operacao
    
    operacao = input(f'Digite o simbolo da operação Matemática para os valores: \n {input_um} \n {input_dois} \n')
    if operacao == 'exit':
        return input_um, input_dois, operacao
    return input_um, input_dois, operacao

def seleciona_operacao(operacao):
    if operacao == '+':
        return soma
    elif operacao == '-':
        return subtrair
    elif operacao == '/':
        return dividir
    elif operacao == '*':
        return multiplicar
    else:
        return 'Operação não permitida'

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
        
        operacao_selecionada = seleciona_operacao(operacao)

        if callable(operacao_selecionada):
            resultado = operacao_selecionada(input_um, input_dois)
        else:
            print(operacao_selecionada)

        if resultado != '':
            print(f'O resultado da operação {operacao} é: {resultado}')