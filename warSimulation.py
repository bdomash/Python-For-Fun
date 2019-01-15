'''
Created on Dec 24, 2016

@author: Brandon
'''
import random
n = 5000
total = 0
winningArr = [0,0,0,0,0]
losingArr = [0,0,0,0,0]
for i in range(n):
    #print "hi"
    p1 = []
    p1winnings = []
    p2 = []
    p2winnings = []
    deck = []
    turns = 0
    wars = 0
    shuffles = [0,0]
    for i in range(2,12):
        for j in range(4):
            deck.append(i)
    for i in range(12):
            deck.append(10)
    random.shuffle(deck)
    arr1 = []
    arr2 = []
    ace1 = 0
    ace2 = 0
    def printPlayer():
        
        print "P1 (" + str(len(p1))+ ") cards:", p1
        print "P2 (" + str(len(p2))+ ") cards:", p2
        print "P1 (" + str(len(p1winnings))+ ") discard:",p1winnings
        print "P2 (" + str(len(p2winnings))+ ") discard:",p2winnings
        print "---------------------------------------------------------"
        
    def deal():
        while len(deck)>0:
            p1.append(deck.pop(0))
            p2.append(deck.pop(0))
        #printPlayer()
        arr1.append(len(p1)+len(p1winnings))
        arr2.append(len(p2)+len(p2winnings))
        for i in p1:
            if i == 11:
                global ace1
                ace1+=1
        for i in p2:
            if i == 11:
                global ace2
                ace2+=1
                
    def reDeck(num):
        global p1
        global p2
        global p1winnings
        global p2winnings
        
        if num == 1:
            #print "Shuffling deck 1"
            shuffles[0]+=1
            p1 = p1winnings
            p1winnings = []
            random.shuffle(p1)
        elif num == 2:
            shuffles[1]+=1
            p2 = p2winnings
            p2winnings = []
            random.shuffle(p2)
            #print "Shuffling deck 2"
        #printPlayer()
        
    def turn():
        #print "Turn #" + str(turns)
        global turns
        if len(p1) == 0:
            reDeck(1)
        if len(p2) == 0:
            reDeck(2)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        turns = turns+1
        
        #print "Player 1's card is:", c1
        #print "Player 2's card is:", c2
        w1=[]
        w2=[]
        r = True
        while r:
            if c1 > c2:
                p1winnings.append(c1)
                p1winnings.append(c2)
                p1winnings.extend(w1)
                p1winnings.extend(w2)
                #print "Player 1 wins"
                r = False
            elif c2 > c1:
                p2winnings.append(c1)
                p2winnings.append(c2)
                p2winnings.extend(w1)
                p2winnings.extend(w2)
                #print "Player 2 wins"
                r = False
            else:
                if (len(p1)==0 and len(p1winnings)==0) or (len(p2)==0 and len(p2winnings)==0):
                    #print "No cards left, cannot war!"
                    p1winnings.extend(w1)      
                    p1winnings.append(c1)
                    p2winnings.extend(w2)
                    p2winnings.append(c2)
                    r = False
                else:
                    #print "War"
                    global wars
                    wars+=1
                    w1.insert(0,c1)
                    w2.insert(0,c2)
                        
                    if len(p1) + len(p1winnings) < 3:
                        while len(p1) > 0:
                            w1.insert(0,p1.pop(0))
                        reDeck(1)
                        while len(p1) > 0:
                            w1.insert(0,p1.pop(0))
                    elif len(p1) < 3:
                        n = 3 - len(p1)
                        while len(p1) > 0:
                            w1.insert(0,p1.pop(0))
                        reDeck(1)
                        for i in range(n):
                            w1.insert(0,p1.pop(0))
                    else:
                        for i in range(3):
                            w1.insert(0,p1.pop(0))
                            
                    if len(p2) + len(p2winnings) < 3:
                        while len(p2) > 0:
                            w2.insert(0,p2.pop(0))
                        reDeck(2)
                        while len(p2) > 0:
                            w2.insert(0,p2.pop(0))
                    elif len(p2) < 3:
                        n = 3 - len(p2)
                        while len(p2) > 0:
                            w2.insert(0,p2.pop(0))
                        reDeck(2)
                        for i in range(n):
                            w2.insert(0,p2.pop(0))
                    else:
                        for i in range(3):
                            w2.insert(0,p2.pop(0))
                    #print "P1 down cards:",w1
                    #print "P2 down cards:",w2
                    c1 = w1.pop(0)
                    c2 = w2.pop(0)
                    #print "P1 up card:",c1
                    #print "P2 up card:",c2
        arr1.append(len(p1)+len(p1winnings))
        arr2.append(len(p2)+len(p2winnings))
        
        
    def gameOver():
        """
        print len(p1)
        print len(p1winnings)
        print len(p2)
        print len(p2winnings)
        """
        if len(p1)==0 and len(p1winnings)==0:
            return True
        elif len(p2)==0 and len(p2winnings)==0:
            return True
        return False
              
    deal()
    while not gameOver():
        turn()
        #printPlayer()
    #print "Game Over"
    if len(p1)==0 and len(p1winnings)==0:
        if ace2 == 0:
            winningArr[0]+=1
        elif ace2 == 1:
            winningArr[1]+=1
        elif ace2 == 2:
            winningArr[2]+=1
        elif ace2 == 3:
            winningArr[3]+=1
        elif ace2 == 4:
            winningArr[4]+=1
        if ace1 == 0:
            losingArr[0]+=1
        elif ace1 == 1:
            losingArr[1]+=1
        elif ace1 == 2:
            losingArr[2]+=1
        elif ace1 == 3:
            losingArr[3]+=1
        elif ace1 == 4:
            losingArr[4]+=1
        #print "Player 2 wins!"
    else:
        if ace1 == 0:
            winningArr[0]+=1
        elif ace1 == 1:
            winningArr[1]+=1
        elif ace1 == 2:
            winningArr[2]+=1
        elif ace1 == 3:
            winningArr[3]+=1
        elif ace1 == 4:
            winningArr[4]+=1
        #print "Player 1 wins!"
        if ace2 == 0:
            losingArr[0]+=1
        elif ace2 == 1:
            losingArr[1]+=1
        elif ace2 == 2:
            losingArr[2]+=1
        elif ace2 == 3:
            losingArr[3]+=1
        elif ace2 == 4:
            losingArr[4]+=1
    turns
    total+=turns
    #print turns
print total/float(n)
print winningArr #array with number of wins by number of aces to start [0,1,2,3,4]
print losingArr  #array with number of losses by number of aces to start [0,1,2,3,4]
arr = [float(winningArr[0])/(winningArr[0]+losingArr[0]),float(winningArr[1])/(winningArr[1]+losingArr[1]),float(winningArr[2])/(winningArr[2]+losingArr[2]),
       float(winningArr[3])/(winningArr[3]+losingArr[3]),float(winningArr[4])/(winningArr[4]+losingArr[4])]
for i in range(len(arr)):
    arr[i]=round(arr[i],3)
    print arr1
    print arr2
print arr
"""
p1 = [2,3,4,2]
p2 = [2,6,3,2,3,4,6,7]
printPlayer()
turn()
printPlayer()
turn()
printPlayer()
"""