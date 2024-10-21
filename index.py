class Pessoa:
     def __init__(self, nome, nacao, lingua):
         self.nome = nome
         self.nacao = nacao
         self.lingua = lingua

pessoas = [
     Pessoa(nome='João', nacao='brasileiro', lingua='português'),
     Pessoa(nome='Anna', nacao='americana', lingua='inglês'),
     Pessoa(nome='Carlos', nacao='espanhol', lingua='espanhol'),
     Pessoa(nome='Maria', nacao='brasileira', lingua='português')
   
]
#regras
for pessoa in pessoas:
     if pessoa.lingua == 'português' and (pessoa.nacao == 'brasileiro' or pessoa.nacao == 'brasileira'):
         print(f'{pessoa.nome} é do Brasil')
     else:
         print(f'{pessoa.nome} não é do Brasil')

for pessoa in pessoas:
    if pessoa.lingua == 'inglês' and (pessoa.nacao == 'americano' or pessoa.nacao == 'americana'):
        print(f'{pessoa.nome} é do EUA')
    else:
        print(f'{pessoa.nome} não é do EUA')

for pessoa in pessoas:
    if pessoa.lingua == 'espanhol' and pessoa.nacao == 'espanhol':
        print(f'{pessoa.nome} é da Espanha')
    else:
        print(f'{pessoa.nome} não é da Espanha')


