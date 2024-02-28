'''
Agora no início iremos ignorar os possíveis erros de entrada de dados
'''

name = input('Qual nome do jogo?\n') #\n vai quebrar a linha
year_launch = int(input('Qual o ano de lançamento do jogo?\n')) 
game_price = float(input('Qual o preço do jogo?\n'))

'''
Colocamos o int e o float nos dois útimos, pois vamos converter para esse tipo de valo, o input retornará um str
'''

print(name)
print(year_launch)
print(game_price)