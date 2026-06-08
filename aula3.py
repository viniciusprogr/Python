# Input
input("Digite seu nome: ")
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")
print(f"Olá, {nome}!") # f-string para formatar a string com a variável nome


numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")



print("A soma dos números é: " + numero1 + numero2) # a variavel numero1 e numero2 são do tipo str, então a operação de soma é uma concatenação de strings
print(f"A soma dos números é: {int(numero1) + int(numero2)}") # a função int() é usada para converter as variáveis numero1 e numero2 de str para int, para que a operação de soma seja realizada corretamente.