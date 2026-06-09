print('Hello, World!')

print(12, 34 , sep='-' ) # sep é um argumento que define o separador entre os valores
print(12, 34 , sep='-' , end='\n $$$$') # end é um argumento que define o que será impresso no final da linha, por padrão é uma quebra de linha (\n)

"""aspas para comentário de múltiplas linhas"""
# comentário de uma linha

"""Python é ua lingugem de tipagem dinamica / forte, ou seja, não é necessário declarar o tipo da variável e o tipo é verificado em tempo de execução"""

# Tipos de dados

#numeros
print(10)

#Strings
#ASPAS SIMPLES
print('Olá, Mundo!')
#ASPAS DUPLAS
print("Olá, Mundo!")
#ASPAS TRIPLAS
print('''Olá, MundoDADADADA!''')

# Booleanos
print(True)

# type serve para verificar o tipo de dado de uma variável ou valor
print(type(10)) # int
print(type(3.14)) # float
print(type('Olá, Mundo!')) # str
print(type(True)) # bool true ou false (verdadeiro ou falso)

print(10 == 10 ) # True verdadeiro == comparação de igualdade
print(10 != 5) # True verdadeiro != comparação de desigualdade
print(10 > 5) # True verdadeiro > comparação de maior que
print(10 < 5) # False falso < comparação de menor que

#concatenação de strings
print('Olá' + ' ' + 'Mundo!') # concatenação de strings com o operador +
print('Olá' , 'Mundo!') # concatenação de strings com o operador ,

#concatenação de int e str
# print('O número é ' + 10 ) # erro de tipo, não é possível concatenar int com str
print('O número é ' + str(10)) # conversão de int para str com a função str()

#concatenação de int
print(10 + 20) # soma de int com o operador +
print(10 - 5) # subtração de int com o operador -
print(10 * 5) # multiplicação de int com o operador *
print(10 / 2) # divisão de int com o operador /, o resultado é um float
print(10 // 3) # divisão inteira de int com o operador //, o resultado é um int
print(10 % 3) # módulo de int com o operador %, o resultado é o resto da divisão inteira
print(10 ** 2) # potência de int com o operador **, o resultado é o número elevado a potência 

# variáveis
x = 10 # declaração de variável x do tipo int
y = 'Olá, Mundo!' # declaração de variável y do tipo str
nome_complerto = 'João da Silva' # declaração de variável nome_completo do tipo str
idade = 30 # declaração de variável idade do tipo int
altura = 1.75 # declaração de variável altura do tipo float

# printar o valor das variáveis
print(x)
print(y)
print('nome:', nome_complerto)
print('idade:', idade)
print('altura:', altura)


# orde de operadores a ser executada
# 1 - parênteses ()
# 2 - exponenciação **
# 3 - multiplicação * e divisão /
# 4 - adição + e subtração -    

consta_1 = 1 + 1 ** 5 + 5
print(consta_1)

consta_1 = (1 + 1) ** (5 + 5)
print(consta_1)

# operadores de comparação
print(10 == 10) # comparação de igualdade, retorna True
print(10 != 5) # comparação de desigualdade, retorna True
print(10 > 5) # comparação de maior que, retorna True
print(10 < 5) # comparação de menor que, retorna False
print(10 >= 10) # comparação de maior ou igual, retorna True
print(10 <= 5) # comparação de menor ou igual, retorna False