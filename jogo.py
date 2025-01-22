print("Hello")
print("Este é um protótipo de um jogo Jokenpo")
print("Insira sua jogada, lembrando que deve ser uma das seguintes opções:")
print("Pedra, Papel ou Tesoura")
print("Boa sorte!")
jogador2 = "Tesoura"
print(jogador2)
jogador1 = input("Digite sua jogada:")
if jogador1 == 'Pedra':
  print("Você ganhou!")
elif jogador1 == 'Papel':
 print("Você perdeu!")
elif jogador1 == 'Tesoura':
  print("Empate!")
else:
 print("Opção inválida tente novamente!")