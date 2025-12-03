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
    return False

def BotMove(place,playerplace):
    playerplace-=1
    i = random.randrange(4)
    if i == 0: #losowy ruch
        for row in range(6):
            if board[row][place]=="0":
                board[row][place] = "O"
                return True
    if i == 1: #przesuniecie jeden w lewo jesli możliwe
        if playerplace ==0:
            for row in range(6):
                if board[row][0]=="0":
                    board[row][0] = "O"
                    return True
        else:
            playerplace-=1
            for row in range(6):
                if board[row][playerplace]=="0":
                    board[row][playerplace] = "O"
                    return True
    if i ==2: #przesuniecie jeden w prawo jesli możliwe
        if playerplace ==6:
            for row in range(6):
                if board[row][6]=="0":
                    board[row][6] = "O"
                    return True
        else:
            playerplace+=1
            for row in range(6):
                if board[row][playerplace]=="0":
                    board[row][playerplace] = "O"
                    return True
    if i == 3: #postawienie X tam gdzie gracz postawił
        for row in range(6):
            if board[row][playerplace]=="0":
                board[row][playerplace] = "O"
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
    
    while True:
        try:
            place = int(input("Gdzie chcesz postawić X? (1-7): "))
            if place < 1 or place > 7:
                print("Podaj liczbę od 1 do 7.")
                continue
            if not PlayerMove(place):
                print("Ta kolumna jest pełna! Wybierz inną.")
                continue
            break
        except ValueError:
            print("To nie jest liczba! Spróbuj ponownie.")
        
    if WinCon("X"):
        BoardPrint()
        print("Wygrałeś!")
        break

    while True:
        bot_choice = random.randrange(7)
        if BotMove(bot_choice, place):
            break
    
    if WinCon("O"):
        BoardPrint()
        print("Przegrałeś!")
        break
    BoardPrint()
