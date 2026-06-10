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

#Operadores lógicos

print('-------------------------------------') # operador lógico AND, retorna True se ambos os operandos forem True
print(True and True) # operador lógico AND, retorna True se ambos os operandos forem True
print(True and False) # operador lógico AND, retorna False se um dos operandos for False
print(True or False) # operador lógico OR, retorna True se um dos operandos for True
print(False or False) # operador lógico OR, retorna False se ambos os operandos forem False
print(not True) # operador lógico NOT, retorna False se o operando for True
print(not False) # operador lógico NOT, retorna True se o operando for False
print('-------------------------------------')

entrada = input("Digite algo: ")
senha_digitanada = input("Digite a senha: ")

senha = "123456"
if( entrada == "verdadeiro" or entrada == "e" ) and senha_digitanada == senha:
    print("A condição é verdadeira")
else:
    print("A condição é falsa")
    

print('-------------------------------------')

#operadores in e not in
print('a' in 'banana') # operador in, retorna True se o valor estiver presente na string
print('x' in 'banana') # operador in, retorna False se o valor não estiver presente na string
print('a' not in 'banana') # operador not in, retorna False se o valor estiver presente na string
print('x' not in 'banana') # operador not in, retorna True se o valor não estiver presente na string



print(30 * "-")

# interpolação de strings e f-strings
nome = "luiz"
preco = 1000.894145155
variavel = '%s, o preço é R$ %.2f' % (nome, preco) # interpolação de strings com o operador % e o tipo de dado, %s para string e %f para float
print(variavel)

#hexadecimal
print('o hexadecimal de 255 é %04x' % 1500) # 

# formataçao de strings e hexadecimal
variavel = 'abc'
print(f'{variavel: >10}.') # interpolação de strings com f-strings, o valor da variável é inserido entre chaves {}
print(f'{variavel: <10}.') 
print(f'{variavel: ^10}.')
print(f'{1000.894145155:.2f}') # formatação de números com f-strings, o valor é formatado com vírgula como separador de milhar e 2 casas decimais
print(f'{1000.894145155:0=+10,.2f}') # formatação de números com f-strings, o valor é formatado com vírgula como separador de milhar, 2 casas decimais, sinal de + para números positivos e preenchimento com zeros à esquerda para ocupar 10 caracteres

#fatiamento de strings
#012345678
#Ola Mundo
#-987654321

print('Ola Mundo'[0]) # fatiamento de strings, retorna o primeiro caractere da string
print('Ola Mundo'[1]) # fatiamento de strings, retorna o segundo caract
print('Ola Mundo'[4:]) # fatiamento de strings, retorna a partir do índice 4 até o final da string
print('Ola Mundo'[:5]) # fatiamento de strings, retorna do início da string até o índice 5 (exclusivo)
print('Ola Mundo'[3:8]) # fatiamento de strings, retorna do índice 3 até o índice 8 (exclusivo)

#len serve para contar o número de caracteres de uma string
variavel = 'Ola Mundo'
print(len(variavel)) # retorna o número de caracteres da string
print(len(variavel[8])) # retorna o número de caracteres da string
