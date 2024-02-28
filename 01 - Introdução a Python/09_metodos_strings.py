game_name = 'Fifa 23'
game_description = '''
Fifa 23 é um jogo de futebol criado pela EA sports 
onde o jogador pode jogar Fifa localmente ou online
'''

#UPPER - Retornará a string toda em maiúsculo 
print(game_name.upper())

#LOWER - Retornará a string toda em minúscolo 
print(game_name.lower())

#TITLE - Retornará a string com a primeira letra maiúsculo, caso seja um texto, todas ficariam maiúscula
print(game_description.title())

#CAPITALIZE - Retornará a primeira letra maiúscula caso ela seja minúsculo e o inverso c.c. *DÚVIDA*
print(game_description.capitalize())

#CENTER - Retornará a string centralizada
print(game_name.center(100, '-')) #Tamanho/Preenchimento

#FIND procura um caractere dentro de uma string
print(game_description.find('a')) #Retorna a posição do primeiro encontrado

#COUNT conta a quantidade de um determinado caractere
print(game_description.count('a'))

#REPLACE troca uma string pela outra
print(game_description.replace('Fifa', 'Pes')) #Trocará todas as ocorrências

#SPLIT  quebra a string por algo, retornando uma lista
print(game_description.split(' '))