'''
## Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex:

fifa 23 → **fi#a 23**

restart→ resta#t

'''

string1 = 'fifa 23'
string2 = 'restart'

print(string1[0] + string1.replace('f', '#', 2)[1:])

print(string2[0] + string2.replace('r', '#', 2)[1:])