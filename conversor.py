num = int(input('Digite um número inteiro: '))
print("""Escolha umas das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin (num)[2:]))
elif opção == 2:
    print('{} convertido em OCTAL é igual a {}.'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}.'.format(num, hex(num)))
else:
    print('Opção invalida')
