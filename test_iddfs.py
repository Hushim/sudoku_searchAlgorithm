import sudoku_iddfs, time

def test1():

    sudoku_iddfs.done=False
    sudoku_iddfs.count =0
    sudoku_iddfs.N=6
    map=[
        [0,0,0,0,4,0],
        [5,0,0,0,0,0], 
        [0,0,2,0,0,4],
        [0,4,0,2,0,0],
        [4,0,0,0,6,0],
        [0,0,6,0,0,0],
        ]
    sudoku_iddfs.display(map)
    t0=time.time()
    r=sudoku_iddfs.IDDFS(map, 0)
    t1=time.time()
    
    if r == 0:
        sudoku_iddfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_iddfs.count))
    else:
        print("no solutions.")


def test2():

    sudoku_iddfs.done=False
    sudoku_iddfs.count =0
    sudoku_iddfs.N=8
    map=[
         [0,0,3,2,0,8,0,6], 
         [6,0,0,0,2,1,0,3],
         [3,0,0,1,0,0,6,8],
         [4,6,0,8,1,0,0,0],
         [0,0,0,3,6,0,1,7],
         [7,0,5,6,8,0,0,0],
         [0,3,0,0,0,6,4,2],
         [0,2,0,4,0,7,0,1],
        ]

    sudoku_iddfs.display(map)
    t0=time.time()
    r=sudoku_iddfs.IDDFS(map, 0)
    t1=time.time()
    
    if r == 0:
        sudoku_iddfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_iddfs.count))
    else:
        print("no solutions.")

def test3():
    sudoku_iddfs.done=False
    sudoku_iddfs.count =0
    sudoku_iddfs.N=9
    map = [
         [0,0,0,0,4,0,6,5,0],
         [0,8,5,0,1,0,4,0,9],
         [9,4,6,0,0,5,0,8,0],
         [0,3,0,9,7,0,0,1,6],
         [8,0,7,0,5,0,9,0,4],
         [0,1,0,4,0,0,7,2,0],
         [0,7,8,0,9,0,3,0,2],
         [6,0,0,0,0,7,8,4,0],
         [4,0,2,0,8,0,0,9,0],
        ]

    sudoku_iddfs.display(map)
    t0=time.time()
    r=sudoku_iddfs.IDDFS(map, 0)
    t1=time.time()
    
    if r == 0:
        sudoku_iddfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_iddfs.count))
    else:
        print("no solutions.")


def test4():
    sudoku_iddfs.done=False
    sudoku_iddfs.count =0
    sudoku_iddfs.N=10
    map=[
        [10,0,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0,0],
        [0,5,0,0,0,7,0,0,0,0],
        [0,0,0,0,4,5,7,0,0,0],
        [0,0,0,1,0,0,0,3,0,0],
        [0,0,1,0,0,0,0,6,8,0],
        [0,0,8,5,0,0,0,1,0,0],
        [0,9,0,0,0,0,4,0,0,0],
        [0,10,0,0,0,0,0,0,0,0],
        ]

    sudoku_iddfs.display(map)
    t0=time.time()
    r=sudoku_iddfs.IDDFS(map, 0)
    t1=time.time()
    
    if r == 0:
        sudoku_iddfs.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_iddfs.count))
    else:
        print("no solutions.")
    


    

if __name__=='__main__':
    test1()
    test2()
    test3()
    test4()
