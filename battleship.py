'''
Created on May 16, 2016

@author: Brandon
'''
from random import randint
turns = 11 #number of misses a player gets in a game
size = 6 #len-1 of the board (a 7x7 board)
board = []
submarine = [] #2-sized boat
destroyer = [] #3-sized boat
battleship = [] #4-sized boat
def setup():
    for x in range(size+1):
        board.append(["O"] * (size+1))
    return board

def print_board(board):
    print "   0 1 2 3 4 5 6"
    print "________________"
    count = 0
    for row in board:
        print str(count) + "| " + " ".join(row)
        count +=1 

def getShip():
    ships = []
 
    
    #ship1: 4 length
    vertIndex = randint(0,1) #0: vertical. 1: horiz
    if vertIndex == 0:
        startRow = randint(0, size-3)
        startCol = randint(0, size)
        ship1 = [[startRow,startCol],[startRow+1,startCol],[startRow+2,startCol],[startRow+3,startCol]]
    else:
        startRow = randint(0, size)
        startCol = randint(0, size-3)
        ship1 = [[startRow,startCol],[startRow,startCol+1],[startRow,startCol+2],[startRow,startCol+3]] 
    ships.append(ship1)
    for i in ship1:
        battleship.append(i)
    #ship2: 3 length
    overlap = True
    c1=1
    while overlap:
        overlap = False
        vertIndex = randint(0,1) #0: vertical. 1: horiz
        if vertIndex == 0:
            startRow = randint(0, size-2)
            startCol = randint(0, size)
            ship2 = [[startRow,startCol],[startRow+1,startCol],[startRow+2,startCol]]       
        else:
            startRow = randint(0, size)
            startCol = randint(0, size-2)
            ship2 = [[startRow,startCol],[startRow,startCol+1],[startRow,startCol+2]] 
        for i in ship1:
            for j in ship2:
                if i == j:
                    overlap = True
                    break
        if not overlap:
            ships.append(ship2)
            for i in ship2:
                destroyer.append(i)
            #print c1
        else:
            c1+=1
             
            
    #ship3: 2 length
    
    overlap = True
    c2=1
    while overlap:
        overlap = False
        vertIndex = randint(0,1) #0: vertical. 1: horiz
        if vertIndex == 0:
            startRow = randint(0, size-1)
            startCol = randint(0, size)
            ship3 = [[startRow,startCol],[startRow+1,startCol]] 
                 
        else:
            startRow = randint(0, size)
            startCol = randint(0, size-1)
            ship3 = [[startRow,startCol],[startRow,startCol+1]] 
        for i in ships:
            for j in i:
                for k in ship3:
                    if k == j:
                        overlap = True
                        break
        if not overlap:
            ships.append(ship3)
            for i in ship3:
                submarine.append(i) 
            #print c2
        else:
            c2+=1

    return ships 
              
    
def playerGuess():
    x = False
    while not x:
        guess_row = -1
        guess_col = -1
        y = False
        while guess_row < 0 or guess_row > size or not y:
            try:
                guess_row = int(raw_input("Guess Row:"))
                y = True
            except ValueError:
                print "Not a valid number"
        y = False
        while guess_col < 0 or guess_col > size or not y:
            try:
                guess_col = int(raw_input("Guess Col:"))
                y = True
            except ValueError:
                print "Not a valid number"
        if board[guess_row][guess_col] == "O":
            x = True
        else:
            print "You've already guess that! Please try again!"
    return [guess_row,guess_col]

    
def handleGuess(s,g):  #returns 0 for hit, 1 for miss     
    hit = False
    cord = []
    for i in s:
        for j in i:
            cord.append(j)
    for i in cord:
        if i == g:
            hit = True
            break
    if hit:
        board[g[0]][g[1]] = "H"
        print "\n\n\nHit!"
        for i in battleship:
            if g == i:
                if len(battleship)==1:
                    print "You have sunk the Battleship!"
                battleship.remove(g)
        for i in destroyer:
            if g == i:
                if len(destroyer)==1:
                    print "You have sunk the Destroyer!"
                destroyer.remove(g)
        for i in submarine:
            if g == i:
                if len(submarine)==1:
                    print "You have sunk the Submarine!"
                submarine.remove(g)
            
        
        return 0
              
    else:
        board[g[0]][g[1]] = "X"
        print "\n\n\nMiss!"
        return 1    

def run():
    setup()
    print_board(board)
    ship = getShip()
    
    #print ship

    t = 0
    hits = 0
    while t < turns and hits < 9:
        if turns-t>1:
            print "You have %s misses remaining" % (turns-t)
        else:
            print "You have %s miss remaining" % (turns-t)
        guess = playerGuess()
        result = handleGuess(ship,guess)
        if result == 0:#hit
            hits += 1
            if hits == 9:
                print "You Win"
        else:
            t+=1
            if t == turns:
                print "You Lose"
                for j in battleship:
                    board[j[0]][j[1]]="B"
                for j in destroyer:
                    board[j[0]][j[1]]="D"
                for j in submarine:
                    board[j[0]][j[1]]="S"
        print_board(board)
        
     
run()

