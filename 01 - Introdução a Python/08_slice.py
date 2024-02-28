game_name = 'Fifa 23'
game_description = '''
Fifa 23 é um jogo de futebol criado pela EA sports
onde o jogador pode jogar localmente ou online
'''

#String [inicio:fim] - Indice começa na posição 0 | indice final -1

#Exemplos:

# 01- Todas strings a partir da primeira posição
print(game_name[0:]) 

# 02- Busque toda string até a ultima posição
print(game_name[:7])

# 03- Busque a string a partir da terceira posição
print(game_name[2:])

'''
string[inicio:fim:passo] -  Indice começa na posição 0 | indice final -1 | passo - determina o incremento.
Por padrão é 1
'''

# 04- Busque toda string de 2 em 2 caractere
print(game_name[::2])

# 05- Busque toda string no indice ímpar
print(game_name[1::2])

# 06- Inverter uma String
print(game_name[::-1])