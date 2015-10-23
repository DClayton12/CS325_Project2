'''
Min Coin Problem
Created on Oct 19, 2015
@author: bparker
'''

#import file argument from command line
#read individual lines ->> conver to lists
import sys
master = []
denfilename = sys.argv[1]
linecount = 0
with open(denfilename) as f:
    for line in f:
        line = line.translate(None, '[],')
        int_list = [int(i) for i in line.split()]        
        master.append(int_list)
        linecount = linecount + 1

fileOutput = open("Amountchange.txt","a")

#changedp():Returns the min amount of coins for amount(A) using coins(V)
#parameters: 
# A = Amount of change to give
# V = denomination of coins
# usedCoins = array to hold coins used. Use this create array of coins used

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



#showCoins(): prints list --> qty of each coin used in min change returned in function changedp();  
#parameters: 
#usedCoins - All coins used for solving each amount of Amount of change from 1 ... n (Amount)
# A = Amount of change to give
def showCoins(usedCoins,A):
    
    str1 = "[" 
    currentA = A - 1
    while currentA > 0:
        
        #go back through the optimal coin solutions, printing which ones we used for Amount of change
        thisCoin = usedCoins[currentA]        
        currentA = currentA - thisCoin
        str1 = str1 + str(thisCoin)         
        str1 = str1  + ','   

    str1 = str1[:-1]
    str1 = str1 + ']'
    print str1
    
    fileOutput.write(str1)
    fileOutput.write("\n")
    
   
     
#loop for every set of input from coin.txt       
for z in range(0,linecount,2):
    V = master[z]
    A = master[z+1][0]
     
    #initialize list, call functions, and show ouput 
    usedCoins = []      
    answer = changedp(A,V,usedCoins)                
    showCoins(usedCoins,A)
    print answer
    str2 = ""
    str2 = str2  + str(answer)
    fileOutput.write(str2)
    fileOutput.write("\n")
    
    

