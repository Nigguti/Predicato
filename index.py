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
def listaLinguistica():
 for pessoa in pessoas:
     if pessoa.lingua == 'português' and (pessoa.nacao == 'brasileiro' or pessoa.nacao == 'brasileira'):
         print(f'\t{pessoa.nome} é {pessoa.nacao}')

 for pessoa in pessoas:
    if pessoa.lingua == 'inglês' and (pessoa.nacao == 'americano' or pessoa.nacao == 'americana'):
        print(f'\t{pessoa.nome} é {pessoa.nacao}')

 for pessoa in pessoas:
    if pessoa.lingua == 'espanhol' and pessoa.nacao == 'espanhol':
        print(f'\t{pessoa.nome} é {pessoa.nacao}')

def fluentePortugues():
    for pessoa in pessoas:
        if pessoa.lingua == 'português':
            print(f'\t{pessoa.nome} fala português')

def definirLinguagem():
    for pessoa in pessoas:
        if pessoa.nome == 'Carlos' and pessoa.nacao == 'espanhol':
            print('\tSim ele é Espanhol')

print('\n\tLista dos fluente em português')
fluentePortugues()

print('\n\tCarlos é espanhol?')
definirLinguagem()

print('\n\tLista das Pessoas:\n')
listaLinguistica()
print('\n')

