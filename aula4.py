# if / elif / else
# se ou se nao se / senao

entrada = input('voce quer entrar? (s/n) ')

if entrada == 's': # se a condição for verdadeira, o bloco de código indentado abaixo será executado
    print('Bem-vindo!')
elif entrada == 'n': # se a condição for falsa, mas a condição elif for verdadeira, o bloco de código indentado abaixo será executado
    print('Até mais!')  
else: # se todas as condições anteriores forem falsas, o bloco de código indentado abaixo será executado
    print('Entrada inválida!')