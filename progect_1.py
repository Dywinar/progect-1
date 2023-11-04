import random
def draw_board(board):
  print(board[0] + "│" + board[1]  + "│"+ board[2])
  print("-+-+-")
  print(board[3] + "│" + board[4]  + "│"+ board[5] )
  print("-+-+-")
  print(board[6] + "│" + board[7]  + "│"+ board[8] )
def get_player_move(board, player):
  while True:
    move = input(f"Игрок {player}, введите номер ячейки от (1-9) ")
    if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
      return int(move) - 1
    else:
      print("Недопустимый ход, попробуйте еще раз")
def get_computer_move(board):
  while True:
    move = random.randint(0, 8)
    if board[move] == " ":
      return move
def check_win(board, player):
  for i in range(3):
    if board[i] == board[i + 3] == board[i +6] == player:
      return True
    if board[i * 3] == board[i*3 + 1] == board[i *3 + 2] == player:
      return True
  if board[0] == board[4] == board[8] == player   or board[2] == board[4]== board[6] == player:
    return True
  return False
def main():
  board = [" "] *9
  players = ['X', 'O']
  turn = 0
  print('Добро пожаловать в игру Крестики-нолики')  
  while True:
    draw_board(board)
    player = players[turn % 2]
    if player == "X":
      move = get_player_move(board, player)
    else:
      print(f"Компьютер {player} делает ход")
      move = get_computer_move(board)
    board[move]= player
    if check_win(board, player):
      draw_board(board)
      return input(f"Поздравляю! Игрок {player} победил. Хотите сыграть еще раз(да/нет)? ")
      break
    elif ' ' not in board:
      draw_board(board) 
      return input("Ничья. Хотите сыграть еще раз(да/нет)? ")
      break
    turn +=1  
while True:
  if main() == 'да':
    continue
  else:
    print('Спасибо за игру')
    break
