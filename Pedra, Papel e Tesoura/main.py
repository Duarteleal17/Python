import random

def play():
    user = input("\nQual é a tua escolha?\n\n").capitalize()
    computer = random.choice(['Pedra', 'Papel', 'Tesoura'])

    print(computer)

    if user == computer:
      return '\nEmpate'

    if is_win(user, computer):
      return '\nO jogador venceu!'

    if is_win(computer, user):
      return '\nO jogador perdeu!'

    else:
      return '\nEscolha inválida!'

def is_win(player, opponent):
  if (player == 'pedra' and opponent == 'Tesoura') or (player == 'Pedra' and opponent == 'Tesoura') \
  or (player == 'tesoura' and opponent == 'Papel') or (player == 'Tesoura' and opponent == 'Papel') \
  or (player == 'papel' and opponent == 'Pedra') or (player == 'Papel' and opponent == 'Pedra'):
    return True

start = "S"
while start != "N":
    
    print(play())
    start = input("\nDesejas jogar denovo (S/N)?\n").capitalize()
