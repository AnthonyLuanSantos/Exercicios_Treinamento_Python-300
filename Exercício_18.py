# Crie duas variáveis com dois valores numéricos inteiros fornecidos pelo usuário,
# caso o valor do primeiro número for maior que o segundo, exiba em tela uma mensagem
# informando que o primeiro número é maior, caso contrário, exiba uma mensagem que
# informe que o segundo número é maior.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo ({num2}).")
else:
    print(f"O segundo número ({num2}) é maior que o primeiro ({num1}).")