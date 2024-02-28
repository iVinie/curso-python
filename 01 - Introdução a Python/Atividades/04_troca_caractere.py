'''

## Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → **xyc abz**
'''
str1 = 'abc'
str2 = 'xyz'

str3 = str2[0:2] + str1[2:] + ' ' + str1[0:2] + str2[2:]
print(str3)