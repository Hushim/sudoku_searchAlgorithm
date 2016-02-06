import string
import copy
import time, sys

# board rule
N = 0
rule={4:[2, 2], 6:[2, 3], 8:[2, 4], 9:[3, 3],10:[2, 5]}

# count the number of recurrence
count=0

# print board (map)
def display(map):
    for i in range(N):
        for j in range(N):
            sys.stdout.write("%d " %map[i][j])
        print("")
    print("")

# check
def check(map, x, y, value):
    for i in range(N): # Check the row
        if map[x][i] == value: return False
        
    for i in range(N): # Ckeck the column
        if map[i][y] == value: return False
        
    xx = x//rule[N][0]*rule[N][0] # xx and yy are the index of small grid
    yy = y//rule[N][1]*rule[N][1] 
    
    # check the small grid
    for i in range(xx, xx+rule[N][0]):
        for j in range(yy, yy+rule[N][1]):
            if map[i][j] == value: return False
    return True

# Iterative DFS
done=False
def IDDFS(map, n):
    global done, count
    count += 1
    
    if n >= N*N: # limit set
        done = True
        return 0
    
    if map[n//N][n%N] != 0: # when reach the limit
        return IDDFS(map, n+1)
    
    for i in range(1, N+1):
        if check(map, n//N, n%N, i):
            map[n//N][n%N] = i
            IDDFS(map, n+1)
            
            if done: return 0
            
            map[n//N][n%N] = 0
    return -1 # no solution    
