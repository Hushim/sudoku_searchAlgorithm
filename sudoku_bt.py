import string
import copy
import time, sys

# board rule
N = 0
rule={4:[2, 2], 6:[2, 3], 8:[2, 4], 9:[3, 3], 10:[2, 5]}

#count the number of rucurrence
count=0

# print the map(board)
def display(map):
    for i in range(N):
        for j in range(N):
            sys.stdout.write("%d " %map[i][j])
        print("")
    print("")

# obtain the value in (x, y)
def getopt(map, i, x, y):
    while(i<=N):
        flag = True
        for j in range(N):
            if map[x][j] == i or map[j][y] == i: # ckeck the row and column
                flag = False
                break
            
            xx = x//rule[N][0]*rule[N][0] + j//rule[N][1]
            yy = y//rule[N][1]*rule[N][1] + j%rule[N][1]
            if map[xx][yy] == i: # check the small grid according to the size of board
                flag = False
                break
        if flag: return i
        i += 1
    return -1

# Backtracking search
def BT(map, x, y):
    global count
    count += 1

    while(map[x][y]!=0):
        y += 1
        if y == N:
            y = 0
            x += 1
            if x == N: return True

    if map[x][y]!=0: return False

    i = getopt(map, 1, x, y) #expand one note
    while(i != -1):
        map[x][y] = i 
        if BT(map, x, y): return True
        map[x][y] = 0 # backtrack if illegal to the rule
        i = getopt(map, i+1, x, y) 
    return False
