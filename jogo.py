print("Hello")
print("Este é um protótipo de um jogo Jokenpo")
print("Insira sua jogada, lembrando que deve ser uma das seguintes opções:")
print("Pedra, Papel ou Tesoura")
print("Boa sorte!")
import random
opcoes = ["Pedra", "Papel", "Tesoura"]
cpu = random.choice(opcoes)
print(cpu)
jogador = input("Digite sua jogada:")
if cpu == jogador:
  print("Empate!")
elif cpu == 'Pedra'and jogador == 'Papel':
  print("Você ganhou!")
elif cpu == 'Pedra'and jogador == 'Tesoura':
  print("Você perdeu!")
elif cpu == 'Papel'and jogador == 'Tesoura':
  print("Você ganhou!")
elif cpu == 'Papel'and jogador == 'Pedra':
  print("Você perdeu!")
elif cpu == 'Tesoura'and jogador == 'Pedra':
  print("Você ganhou!")
elif cpu == 'Tesoura'and jogador == 'Papel':
  print("Você perdeu!")
else:
    print("Opção inválida tente novamente!")