import sudoku_dfs, time

def test1():
   
    sudoku_dfs.count = 0
    sudoku_dfs.N=6
    map=[
        0,0,0,0,4,0,
        5,0,0,0,0,0, 
        0,0,2,0,0,4,
        0,4,0,2,0,0,
        4,0,0,0,6,0,
        0,0,6,0,0,0,
        ]
    points=sudoku_dfs.init(map)
    
    sudoku_dfs.display(map)
    t0=time.time()
    p=points.pop()
    r=sudoku_dfs.DFS(p,map, points)
    t1=time.time()
    
    if r:
        sudoku_dfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_dfs.count))
    else:
        print("no solutions.")
    
    
def test2():
        
    sudoku_dfs.count = 0
    sudoku_dfs.N=8
    map=[
        1,0,0,0,0,0,0,0,
        0,0,0,0,0,0,7,0,
        0,0,2,0,7,4,0,0,
        4,0,0,8,0,3,0,0,
        0,0,0,0,6,5,0,0,
        0,1,0,0,0,0,0,0,
        0,3,0,0,5,0,0,0,
        0,2,6,0,0,0,8,0,
        ]

    points=sudoku_dfs.init(map)
    
    sudoku_dfs.display(map)
    t0=time.time()
    p=points.pop()
    r=sudoku_dfs.DFS(p,map, points)
    t1=time.time()
    
    if r:
        sudoku_dfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_dfs.count))
    else:
        print("no solutions.")

def test3():
    sudoku_dfs.count = 0
    sudoku_dfs.N=9
    map=[
        0,0,0,8,4,0,6,5,0,
        0,8,0,0,0,0,0,0,9,
        0,0,0,0,0,5,2,0,1,
        0,3,4,0,7,0,5,0,6,
        0,6,0,2,5,1,0,3,0,
        5,0,9,0,6,0,7,2,0,
        1,0,0,5,0,0,0,0,0,
        6,0,0,0,0,0,0,4,0,
        0,5,0,0,8,0,0,0,0,
        ]
    points=sudoku_dfs.init(map)
    
    sudoku_dfs.display(map)
    t0=time.time()
    p=points.pop()
    r=sudoku_dfs.DFS(p,map, points)
    t1=time.time()
    
    if r:
        sudoku_dfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_dfs.count))
    else:
        print("no solutions.")   

def test4():
    sudoku_dfs.count = 0
    sudoku_dfs.N=10
    map=[
        10,0,0,0,0,0,0,0,0,0,
        0,0,3,6,0,0,0,0,0,0,
        0,7,0,0,9,0,2,0,0,0,
        0,5,0,0,0,7,0,0,0,0,
        0,0,0,0,4,5,7,0,0,0,
        0,0,0,1,0,0,0,3,0,0,
        0,0,1,0,0,0,0,6,8,0,
        0,0,8,5,0,0,0,1,0,0,
        0,9,0,0,0,0,4,0,0,0,
        0,10,0,0,0,0,0,0,0,0,
    ]

    points=sudoku_dfs.init(map)
    
    sudoku_dfs.display(map)
    t0=time.time()
    p=points.pop()
    r=sudoku_dfs.DFS(p,map, points)
    t1=time.time()
    
    if r:
        sudoku_dfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_dfs.count))
    else:
        print("no solutions.")



    
    
    

if __name__=='__main__':
    test1()
    test2()
    test3()
    test4()
