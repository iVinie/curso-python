'''
Agora no início iremos ignorar os possíveis erros de entrada de dados
'''

name = input('Qual nome do jogo?\n') 
year_launch = int(input('Qual o ano de lançamento do jogo?\n')) 
game_price = float(input('Qual o preço do jogo?\n'))

print('####Dados do Jogo####')
print('=====================')

#Alternativa 1
print('Nome do jogo: ', name)
print('Ano de lançamento do jogo: ', year_launch)
print('Preço do jogo: ' ,game_price)

#Alternativa 2
print('Nome do jogo: ', name, '\nAno de lançamento do jogo: ', year_launch, '\nPreço do jogo: ' ,game_price)

#Alternativa 3
'''A Mais utilizada'''

print(f'Nome do jogo: {name}\n Ano de lançamento do jogo: {year_launch}\n Preço do jogo: {game_price}')