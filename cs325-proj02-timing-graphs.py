# CS325 - Project 2 - Coin Change
# Main py file to test accuracy of data from inputfile
# Group 9: Darnel Clayton, Rudy Gonzalez, Brad Parker

import sys
import time
sys.setrecursionlimit(1500)

'''
ALGORITHM 1 - Brute Force Recursion
'''

def changeslow(A, V, cindex):
    if A == 0:
        return 0
    if cindex == len(V):
        return sys.maxsize
    if A < V[cindex]:
        return changeslow(A, V, cindex+1)
    else:
        c1 = changeslow(A, V, cindex+1)
        c2 = 1 + changeslow(A-V[cindex], V, cindex)
        if c1 < c2:
            return c1
        else:
            return c2


'''
ALGORITHM 2 - Greedy Approach
'''

def changegreedy(A, V):
    coins_given = [0]*len(V)
    numcoins = 0 #number of coins per denomination

    amount_remaining = A

    coin_index = len(V) - 1
    max_coin = V[coin_index] #set to last element in coins

    while amount_remaining > 0:

        if max_coin <= amount_remaining:
            amount_remaining -= max_coin
            numcoins += 1
            coins_given[coin_index] = numcoins
        else:
            coin_index -= 1
            max_coin = V[coin_index]
            numcoins = 0

    #counts the total number of coins given
    min_coins = 0
    for i in range(0, len(V)):
        min_coins += coins_given[i]

    return coins_given, min_coins


'''
ALGORITHM 3 - Dynamic Programming Approach
'''

def changedp(A,V,usedCoins):

    sol = [0 for x in range(A+1)]                                   #initilize list of solutions; s[] is our solution of min coins for each amount
    sol[0] = 0                                                      #solution @ 0 is always 0

    for x in range(1,A+1):                                          #solve for every value from 1 ... n (Amount)
        sol[x] = 99999                                              #initialize max integer for comparison
        storeCoin = 0

        for y in range(len(V)):                                     #Try every coin(x) for every amount(y)

            if (x >= V[y]) and (1 + sol[x-V[y]] < sol[x]):          #if amount(x) is >= coin(y) AND 1 + best solutiion[go back amount of coin] < best current solution
                newValue = 1 + sol[x-V[y]]                          #record this solution as best so far
                sol[x] = newValue
                storeCoin = V[y]

        usedCoins.append(storeCoin)                                 #record the coin to show later in output

    return sol[x]


def showCoins(usedCoins,A,V):

    coins_given = [0]*len(V)
    currentA = A - 1
    while currentA > 0:

        #go back through the optimal coin solutions, printing which ones we used for Amount of change
        thisCoin = usedCoins[currentA]
        currentA = currentA - thisCoin

        coin_index = V.index(thisCoin)
        coins_given[coin_index] += 1

    return coins_given


'''
TEST CODE FOR MIN COINS - QUESTIONS 4 - 6
'''
print("processing min coin tests for questions 4-6...")
'''
Question 4: changegreedy and changedp ranges 2010-2200
'''
#changegreedy
testrange = "2010-2200"
outputfile = testrange + "change.txt"
f = open(outputfile, "w")
f.write("changegreedy min coin results for " + testrange + ":\n")
V = [1, 5, 10, 25, 50]

for A in range(2010, 2205, 5):
    coins_given = []
    min_coins = 0
    coins_given, min_coins = changegreedy(A, V)
    f.write(str(min_coins) + "\n")
f.write("\n")

#changedp
f.write("changedp min coin results:\n")
for A in range(2010, 2205, 5):
    coins_given = []
    min_coins = 0
    usedCoins = []
    min_coins = changedp(A,V,usedCoins)
    f.write(str(min_coins) + "\n")
f.write("\n")

f.close()


'''
Question 5: changegreedy and changedp ranges 2000-2200
'''
#changegreedy
testrange = "2000-2200"
outputfile = testrange + "change.txt"
f = open(outputfile, "w")
f.write("changegreedy min coin results for " + testrange + " and V1 = [1, 2, 6, 12, 24, 48, 60] :\n")
V1 = [1, 2, 6, 12, 24, 48, 60]

for A in range(2000, 2201, 1):
    coins_given = []
    min_coins = 0
    coins_given, min_coins = changegreedy(A, V1)
    f.write(str(min_coins) + "\n")
f.write("\n")


#changedp
f.write("changedp min coin results:\n")
for A in range(2000, 2201, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    min_coins = changedp(A,V1,usedCoins)
    f.write(str(min_coins) + "\n")
f.write("\n")

f.write("changegreedy min coin results for " + testrange + " and V2 = [1, 6, 13, 37, 150] :\n")
V2 = [1, 6, 13, 37, 150]

for A in range(2000, 2201, 1):
    coins_given = []
    min_coins = 0
    coins_given, min_coins = changegreedy(A, V2)
    f.write(str(min_coins) + "\n")
f.write("\n")


#changedp
f.write("changedp min coin results:\n")
for A in range(2000, 2201, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    min_coins = changedp(A,V2,usedCoins)
    f.write(str(min_coins) + "\n")
f.write("\n")

f.close()



'''
Question 6: changegreedy and changedp ranges 2000-2200
V=[1, 2, 4, 6, 8, 10, 12, to 30]
'''
#changegreedy
testrange = "2000-2200b"
outputfile = testrange + "change.txt"
f = open(outputfile, "w")
f.write("changegreedy min coin results for " + testrange + " and V = [1, 2, 4, 6, 8, 10, 12 to 30] :\n")
V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

for A in range(2000, 2201, 1):
    coins_given = []
    min_coins = 0
    coins_given, min_coins = changegreedy(A, V)
    f.write(str(min_coins) + "\n")
f.write("\n")


#changedp
f.write("changedp min coin results:\n")
for A in range(2000, 2201, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    min_coins = changedp(A,V,usedCoins)
    f.write(str(min_coins) + "\n")
f.write("\n")

f.close()

'''
Question 6: changegreedy, changedp and changeslow ranges 5-40
Purpose is to show all on one graph
V = [1, 2, 6, 12, 24, 48, 60]
'''
#changegreedy
testrange = "5-40"
outputfile = testrange + "change.txt"
f = open(outputfile, "w")
f.write("changegreedy min coin results for " + testrange + " and V = [1, 2, 6, 12, 24, 48, 60]:\n")
V = [1, 2, 6, 12, 24, 48, 60]

for A in range(5, 41, 1):
    coins_given = []
    min_coins = 0
    coins_given, min_coins = changegreedy(A, V)
    f.write(str(min_coins) + "\n")
f.write("\n")


#changedp
f.write("changedp min coin results:\n")
for A in range(5, 41, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    min_coins = changedp(A,V,usedCoins)
    f.write(str(min_coins) + "\n")
f.write("\n")


#changeslow
f.write("changeslow min coin results:\n")
for A in range(5, 41, 1):
    coins_given = []
    min_coins = 0
    min_coins = changeslow(A, V, 0)
    f.write(str(min_coins) + "\n")
f.write("\n")

f.close()

print("Tests completed. Results written to output files.")


'''
TEST CODE FOR TIMING - QUESTIONS 4 - 6
'''
print("processing timing tests for questions 4-6...")

'''
Question 4: changegreedy, changedp and changeslow timing
'''
#changegreedy
testrange = "100000-100100"
timingfile = "timing-q04-" + testrange + ".txt"
t = open(timingfile, "w")
t.write("changegreedy timing results for " + testrange + ":\n")
V = [1, 5, 10, 25, 50]

for A in range(100000, 100100, 1):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    coins_given, min_coins = changegreedy(A, V)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")

#changedp
t.write("changedp timing results:\n")
for A in range(100000, 100100, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    start_time = time.time()
    min_coins = changedp(A,V,usedCoins)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")
t.close()


'''
Question 5: changegreedy and changedp timing
'''
#changegreedy
testrange = "100000-100100"
timingfile = "timing-q05-" + testrange + ".txt"
t = open(timingfile, "w")
t.write("changegreedy timing results for " + testrange + " and V1 = [1, 2, 6, 12, 24, 48, 60] :\n")
V1 = [1, 2, 6, 12, 24, 48, 60]

for A in range(100000, 100100, 1):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    coins_given, min_coins = changegreedy(A, V1)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")

#changedp
t.write("changedp timing results:\n")
for A in range(100000, 100100, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    start_time = time.time()
    min_coins = changedp(A,V1,usedCoins)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")

t.write("changegreedy timing results for " + testrange + " and V2 = [1, 6, 13, 37, 150] :\n")
V2 = [1, 6, 13, 37, 150]

for A in range(100000, 100100, 1):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    coins_given, min_coins = changegreedy(A, V2)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")

#changedp
t.write("changedp timing results:\n")
for A in range(100000, 100100, 1):
    coins_given = []
    min_coins = 0
    usedCoins = []
    start_time = time.time()
    min_coins = changedp(A,V2,usedCoins)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")
t.close()


'''
Question 6: changegreedy, changedp and changeslow timing
V=[1, 2, 4, 6, 8, 10, 12, to 30]
'''


#changegreedy
testrange = "100000-10000000"
timingfile = "timing-q06-" + testrange + ".txt"
t = open(timingfile, "w")

t.write("changegreedy timing results for " + testrange + " and V = [1, 2, 4, 6, 8, 10, 12 to 30] :\n")
V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

for A in range(100000, 10100000, 100000):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    coins_given, min_coins = changegreedy(A, V)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")


#changedp
t.write("changedp timing results:\n")
for A in range(100000, 10100000, 100000):
    coins_given = []
    min_coins = 0
    usedCoins = []
    start_time = time.time()
    min_coins = changedp(A,V,usedCoins)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")


#changeslow
t.write("changeslow timing results - range 50-100:\n")
for A in range(50, 101, 1):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    min_coins = changeslow(A, V, 0)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")

t.close()

print("Tests completed. Results written to output files.")


'''
Question 8: changegreedy, changedp and changeslow timing
V=[1, 5, 10, 25, 50]
'''

#changegreedy
testrange = "100000-10000000"
timingfile = "timing-q08-" + testrange + ".txt"
t = open(timingfile, "w")

t.write("changegreedy timing results for " + testrange + " and V = [1, 2, 4, 6, 8, 10, 12 to 30] :\n")
V = [1, 5, 10, 25, 50]

for A in range(100000, 10100000, 100000):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    coins_given, min_coins = changegreedy(A, V)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")


#changedp
t.write("changedp timing results:\n")
for A in range(100000, 10100000, 100000):
    coins_given = []
    min_coins = 0
    usedCoins = []
    start_time = time.time()
    min_coins = changedp(A,V,usedCoins)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")


#changeslow
t.write("changeslow timing results - range 50-100:\n")
for A in range(50, 101, 1):
    coins_given = []
    min_coins = 0
    start_time = time.time()
    min_coins = changeslow(A, V, 0)
    run_time = (time.time() - start_time) * 1000 #converts to msec
    t.write(str(run_time) + "\n")
t.write("\n")

t.close()

print("Tests completed. Results written to output files.")