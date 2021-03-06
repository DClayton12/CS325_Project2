# CS325 - Project 2 - Coin Change
# Main py file to test accuracy of data from inputfile
# Group 9: Darnel Clayton, Rudy Gonzalez, Brad Parker

import sys
import time
sys.setrecursionlimit(1500)

'''
LOADS FILE INPUT WITH TEST PROBLEMS FROM COMMAND LINE
'''
inputfile = sys.argv[1]
inputarray = []

#read in arrays from text file
def load_inputarray():
    with open(inputfile) as f:
        linenum = 1
        for line in f:
            if linenum % 2 != 0: #checks if linenum is odd
                numarray = []
                numstring = line.strip().replace("'", "").replace("[", "").replace("]", "").replace(",", " ")
                numbers = map(int, numstring.split())

                for num in numbers:
                    numarray.append(num)
                inputarray.append(numarray)
            else:
                amount = line.strip().replace("'", "")
                inputarray.append(int(amount))
            linenum += 1

    f.close()
load_inputarray()


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
RUN CODE FOR INPUT FILE PROBLEMS
'''
outputfile = inputfile.replace(".txt", "") + "change.txt"
f = open(outputfile, "w")


#runs tests for changeslow
print("changeslow results:")
f.write("changeslow results:\n")
for i in range(0, len(inputarray)-1, 2):
    V = inputarray[i]
    A = inputarray[i+1]
    coins_given = []
    min_coins = 0
    min_coins = changeslow(A, V, 0)
    #print(coins_given)
    print(min_coins)
    f.write(str(min_coins) + "\n\n")
print("")


#runs tests for changegreedy
print("changegreedy results:")
f.write("changegreedy results:\n")
for i in range(0, len(inputarray)-1, 2):
    V = inputarray[i]
    A = inputarray[i+1]
    coins_given = []
    min_coins = 0
    coins_given, min_coins = changegreedy(A, V)
    print(coins_given)
    print(min_coins)
    f.write(str(coins_given)+ "\n")
    f.write(str(min_coins) + "\n\n")
print("")


#runs tests for changedp
print("changedp results:")
f.write("changedp results:\n")
for i in range(0, len(inputarray)-1, 2):
    V = inputarray[i]
    A = inputarray[i+1]
    coins_given = []
    min_coins = 0

    usedCoins = []
    min_coins = changedp(A,V,usedCoins)
    coins_given = showCoins(usedCoins,A,V)

    print(coins_given)
    print(min_coins)
    f.write(str(coins_given) + "\n")
    f.write(str(min_coins) + "\n\n")
print("")

f.close()

print("Tests completed. Results written to " + outputfile + " file.")