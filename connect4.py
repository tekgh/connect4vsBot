import random

board = [["0" for _ in range(7)] for _ in range(6)]
def BoardPrint():
    for row in range(5, -1, -1):
        print(board[row])

def PlayerMove(place):
    for row in range(6):
        if board[row][place]=="0":
            board[row][place] = "X"
            return True
    return False

def BotMove(RandomPlace,playerplace):
    i = random.randrange(4)

    #losowy ruch
    if i == 0: 
        move = RandomPlace

    #przesuniecie jeden w lewo jesli możliwe
    if i == 1:
        if playerplace ==0:
            move = 0
        else:
            move = playerplace-1

    #przesuniecie jeden w prawo jesli możliwe
    if i ==2:
        if playerplace ==6:
            move = 6
        else:
            move = playerplace+1

    #postawienie X tam gdzie gracz postawił
    if i == 3:
        move = playerplace
    for row in range(6):
            if board[row][move]=="0":
                board[row][move] = "O"       
                return True
    return False

def WinCon(player):
    #poziom
    for row in range (6):
        for col in range(4):
            if all(board[row][col+i] ==player for i in range(4)):
                return True
            
    #pion
    for row in range (3):
        for col in range(7):
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
    #ruch gracza
    while True:
        try:
            place = int(input("Gdzie chcesz postawić X? (1-7): "))-1
            if place < 0 or place > 6:
                print("Podaj liczbę od 1 do 7.")
                continue
            if not PlayerMove(place):
                print("Ta kolumna jest pełna! Wybierz inną.")
                continue
            break
        except ValueError:
            print("To nie jest liczba! Spróbuj ponownie.")
    #sprawdzenie czy gracz wygrał
    if WinCon("X"):
        BoardPrint()
        print("Wygrałeś!")
        break
    
    #ruch bota
    while True:
        bot_choice = random.randrange(7)
        if BotMove(bot_choice, place):
            break
        
    #sprawdzenie czy bot wygrał
    if WinCon("O"):
        BoardPrint()
        print("Przegrałeś!")
        break
    BoardPrint()
