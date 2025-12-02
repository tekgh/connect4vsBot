import random
board = [["0" for _ in range(7)] for _ in range(6)]
def BoardPrint():
    for row in range(5, -1, -1):
        print(board[row])

def PlayerMove(place):
    place-=1
    for row in range(6):
        if board[row][place]=="0":
            board[row][place] = "X"
            return True
    return print("Chcesz wyjść za mape!") #trzeba dać użytkonikowi ruch jak się stara wyjść za mape

def BotMove(place):
    for row in range(6):
        if board[row][place]=="0":
            board[row][place] = "O"
            return True
    return False

def WinCon(player):
    #poziom
    for row in range (6):
        for col in range(4):
            if all(board[row][col+i] ==player for i in range(4)):
                return True
    #pion
    for row in range (7):
        for col in range(3):
            if all(board[row+i][col] == player for i in range(4)):
                return True
    #skos/
    for row in range (4):
        for col in range(3):
            if all(board[row+i][col+i] == player for i in range(4)):
                return True
    #skos\
    for row in range (3):
        for col in range(3,7):
            if all(board[row+i][col-i] == player for i in range(4)):
                return True
    return False
    
     
#Główny program
BoardPrint()
while(1):
    place=int(input("Gdzie chcesz postawić X?(1-7): "))
    PlayerMove(place)
    if WinCon("X"):
        BoardPrint()
        print("Wygrałeś!")
        break
    BotMove(random.randrange(7))
    if WinCon("O"):
        BoardPrint()
        print("Przegrałeś!")
        break
    BoardPrint()
