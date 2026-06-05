nome = "Maria Silva" # declaração de variável nome do tipo str
altura = 1.80 # declaração de variável altura do tipo float
peso = 95 # declaração de variável peso do tipo int
imc = peso / (altura ** 2) # cálculo do IMC com a fórmula peso / altura ao quadrado
print('nome:', nome)
print('altura:', altura)
print('peso:', peso)
print('IMC:', imc)

# Formatação de string usando f-string para exibir as informações de forma organizada

linha1 = f'Olá, meu nome é {nome}' 
linha2 = f' tenho {altura:.2f} metros de altura e peso {peso} kg.'
linha3 = f'Meu IMC é {imc:.2f}.' 

print(linha1)
print(linha2)
print(linha3)