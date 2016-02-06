import sys
# board rule
N = 0
rule={4:[2, 2], 6:[2, 3], 8:[2, 4], 9:[3, 3], 10:[2, 5]}

# count the number of recurrence
count=0

# points in board
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.option=[]
        self.value=0

def ROW(p, map):
    row=set(map[p.y*N:(p.y+1)*N])
    row.remove(0)
    return row

def COL(p,map):
    col=[]
    length=len(map)
    for i in range(p.x,length,N):
        col.append(map[i])
    col=set(col)
    col.remove(0)
    return col

def BLOCK(p,map):
    x=p.x//rule[N][1]
    y=p.y//rule[N][0]
    block=[]
    start=y*rule[N][0]*N+x*rule[N][1]
	
    for i in range(0, rule[N][0]):
        for j in range(start+i*N, start+i*N+rule[N][1]):
            block.append(map[j])
        
    block=set(block)
    block.remove(0)
    return block

# initial
def init(map):
    list=[]
    n=len(map)
    for i in range(n):
        if map[i]==0:
            p=point(i%N,i//N)
            for j in range(1,N+1):
                if j not in ROW(p,map) and j not in COL(p,map) and j not in BLOCK(p,map):
                    p.option.append(j)
            list.append(p)
    return list

def check(p,map):
    if p.value==0:
        return False
    
    return p.value not in ROW(p,map) and p.value not in COL(p,map) and p.value not in BLOCK(p,map)

# DFS
def DFS(p,map, points):
    global count
    count+=1
    opt=p.option
    for v in opt: # expand notes
        p.value=v
        if check(p,map):
            map[p.y*N+p.x]=p.value
            if len(points)<=0:
                return True # exit
            
            p2=points.pop()
            if DFS(p2,map, points): # Depth-first recurrence
                return True
            
            map[p2.y*N+p2.x]=0
            map[p.y*N+p.x]=0
            p2.value=0
            points.append(p2)
    return False

# display board
def display(map):
    for j in range(N):
        for i in range(N):
            sys.stdout.write("%d " %(map[j*N+i]))
        print("")
    print("")    
