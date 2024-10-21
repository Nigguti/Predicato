class Pessoa:
     def __init__(self, nome, nacao, lingua):
         self.nome = nome
         self.nacao = nacao
         self.lingua = lingua

pessoas = [
     Pessoa(nome='João', nacao='brasileiro', lingua='português'),
     Pessoa(nome='Anna', nacao='americana', lingua='inglês'),
     Pessoa(nome='Carlos', nacao='espanhol', lingua='espanho'),
     Pessoa(nome='Maria', nacao='brasileira', lingua='português')
]