# Peça para que o usuário digite um número, em seguida o converta para float,
# exibindo em tela tanto o número em si quanto seu tipo de dado.

num = input("Digite um número: ")
numfloat = float(num)
print(f"O número digitado é: {numfloat}")
print(f"Tipo: {type(numfloat)}")