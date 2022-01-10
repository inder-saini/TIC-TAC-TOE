import collections
import random


def tic_tac_toe(values):

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}   | {}".format(values[0],values[1],values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}   | {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}   | {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


def choose_sign(player1,player2):
    number = random.randint(0,1)
    Player1 = ""
    Player2 = ""
    while True:
     try:
        print("To play the game, choose 1.")
        print("To quit the game enter 2.")
        print("What is your choice:")
        choice = int(input())

        if(choice == 1):
         if(number == 0):
          print("The first player is {}".format(player1))
          cur_player = player1
          next_player = player2
         else:
          print("The first player is {}".format(player2))
          cur_player = player2
          next_player = player1


         cur_player_sign = input("Enter the sign you want to choose: X or O")
         if (cur_player_sign == 'X'):
            Player1 = 'X'
            print("The {0} has chosen {1}".format((cur_player),(cur_player_sign)))
            Player2 = 'O'

         elif(cur_player_sign == 'O'):
            Player1 = 'O'
            print("The {0} has chosen {1}".format((cur_player), (cur_player_sign)))
            Player2 ='X'
         return game(cur_player, Player1,next_player,Player2)
        elif(choice == 2):
            break
        elif(choice != 1) or (choice != 2):
            print("Wrong Input. Enter Again!!")
     except ValueError:
        print("Wrong Input")
        continue

def game(cur_player,sign1, next_player,sign2):
    scoreboard = {'player1':[],'player2':[]}
    values = ['' for x in range(9)]
    player_pos = {'X':[], 'O':[]}

    while True:
        tic_tac_toe(values)

        try:
            print(" Current Player is:", cur_player,"with sign:",sign1)
            move = int(input())
        except ValueError:
            print("Wrong Input!! Try again")
            continue
        if(move <1) or(move>9):
             print("Wrong Input!! Try Again")
        if values[move-1]!= '':
             print("The place is already filled.")
             continue
        values[move-1] = sign1

        player_pos[sign1].append(move)

        if check_win(player_pos, sign1):
            tic_tac_toe(values)
            #scoreboard = player_pos[sign1].
            print("The game is won by ",cur_player," with sign",sign1)
            print("\n")
            return cur_player

        if check_draw(player_pos):
            tic_tac_toe(values)
            print("Game has been drawn")
            print("\n")
            return 'D'

        if(sign1 == 'X'):
            temp = cur_player
            cur_player = next_player
            next_player = temp
            sign1 = 'O'
        elif(sign1 == 'O'):
            temp = cur_player
            cur_player = next_player
            next_player = temp
            sign1= 'X'





def check_win(player_pos,cur_player):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in solution:
        if all(y in player_pos[cur_player] for y in x):
          return True
    return False

def check_draw(player_pos):
    if (len(player_pos['X']) + len(player_pos['O'])) == 9:
        return True
    return False


if __name__ == "__main__":

    while True:
     player1 = input("Player 1's Name:")
     player2 = input("Player 2's Name:")
     choose_sign(player1,player2)

     try:

         print("If you want to play again, press 1")
         print("If you want to quit press 2")
         choice = int(input())
         if(choice ==1):
           choose_sign(player1, player2)
         elif(choice == 2):
             break
         elif (choice != 1) or (choice != 2):
           print("Wrong Input. Enter Again!!")
     except ValueError:
      print("Wrong Input")
      continue







