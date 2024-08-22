def maior(primeiro_numero, segundo_numero):
    if primeiro_numero > segundo_numero:
        print(f'{primeiro_numero} é maior que {segundo_numero}')
    else:
        print(f'{primeiro_numero} não é maior que {segundo_numero}')

def menor(primeiro_numero, segundo_numero):
    if primeiro_numero < segundo_numero:
        print(f'{primeiro_numero} é menor que {segundo_numero}')
    else:
        print(f'{primeiro_numero} não é menor que {segundo_numero}')

def igual(primeiro_numero, segundo_numero):
    if primeiro_numero == segundo_numero:
        print(f'{primeiro_numero} é igual a {segundo_numero}')
    else:
        print(f'{primeiro_numero} não é igual a {segundo_numero}')

def seleciona_operacao(operacao):

    if operacao == '>':
         return maior
    elif operacao == '<':
        return menor
    elif operacao == '=':
        return igual
    
def funcao_calculadora(primeiro_numero, segundo_numero, operacao, operacao_selecionada):
    operacao = input('Digite a operação matemática: \n')
    if operacao == 'exit':
        return 'exit'
    operacao_selecionada = seleciona_operacao(operacao)
    primeiro_numero = input('Digite o primeiro número da operação: \n')
    if primeiro_numero == 'exit':
        return 'exit'
    else:
        primeiro_numero = float(primeiro_numero)
    segundo_numero = input('Digite o segundo número para a operação: \n')
    if segundo_numero == 'exit':
        return 'exit'
    else:
        segundo_numero = float(segundo_numero)
    if callable(operacao_selecionada):
        operacao_selecionada(primeiro_numero, segundo_numero)
    else:
        print("Operação não existe!")
    return 'haha'

operacao = ''
primeiro_numero = 0
segundo_numero = 0
operacao_selecionada = ''
saida = 'exit'

while saida == 'exit':
    saida = funcao_calculadora(primeiro_numero, segundo_numero, operacao, operacao_selecionada)