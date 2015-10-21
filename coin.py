__author__ = 'darnelclayton'

*****PSEUDOCODE******


***ALG01 - changeslow***




***ALGO2 - changegreedy***

Coins = [V1, v2, ... Vn] //sorted denominations

changegreedy (Amount, Coins)
    coins_given = []
    numcoins = 0 //number of coins per denomination

    for i = 0 to Coins.length - 1
        coins_given[i] to numcoins //initializes array of coins given to 0
    amount_remaining = Amount

coin_index = Coins.length - 1
max_coin = Coins[coin_index] //set to last element in coins

while amount_remaining > 0

    if max_coin <= amount_remaining
        amount_remaining = amount_remaining - max_coin
        numcoins = numcoins + 1
        coins_given[coin_index] = numcoins
    else
        coin_index = coin_index - 1
        max_coin = Coins[coin_index]

//counts the total number of coins given
min_coins = 0
for i = 0 to Coins.length - 1
    min_coins = min_coins + coins_given[i]

return coins_given, min_coins



***ALG03 - changedp***




******CODE*********

# CS325 - Project 2 - Coin Change
#Group 9: Darnel Clayton, Rudy Gonzalez, Brad Parker

import sys

sys.setrecursionlimit(1500)
inputfile = "coin1.txt"
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


# Algorithm 1 - brute force recursive

def changeslow(A, V):

    ####INSERT CODE#####

    return


# Algorithm 2 - greedy
def changegreedy(A, V):

    ####INSERT CODE#####

    return


# Algorithm 3 - dynamic programming
def changedp(A, V):

    ####INSERT CODE#####

    return


#runs tests for changeslow
print("changeslow results:")
for i in range(0, len(inputarray)-1, 2):
    V = inputarray[i]
    A = inputarray[i+1]
    changeslow(A, V)
print()

#runs tests for changeslow
print("changegreedy results:")
for i in range(0, len(inputarray)-1, 2):
    V = inputarray[i]
    A = inputarray[i+1]
    changeslow(A, V)
print()

#runs tests for changeslow
print("changedp results:")
for i in range(0, len(inputarray)-1, 2):
    V = inputarray[i]
    A = inputarray[i+1]
    changeslow(A, V)
print()


**************************
BRAD'S INSERTED CODE BELOW:

Created on Oct 19, 2015

@author: bparker
'''

A = 67
V = [1,5,10,25]
usedCoins = []

def makechange(A,V,usedCoins):

    sol = [0 for x in range(A+1)]                               #initilize list of solutions
    sol[0] = 0

    for x in range(1,A+1):
        sol[x] = 99999

        storeCoin = 0
        for y in range(len(V)):


            if (x >= V[y]) and (1 + sol[x-V[y]] < sol[x]):
                newValue = 1 + sol[x-V[y]]
                sol[x] = newValue
                storeCoin = V[y]

        usedCoins.append(storeCoin)



    return sol[x]


def showCoins(usedCoins,A):

    coin = A - 1
    while coin > 0:
        thisCoin = usedCoins[coin]
        print thisCoin
        coin = coin - thisCoin





answer = makechange(A,V,usedCoins)
print "*****"
print answer
showCoins(usedCoins,A)
