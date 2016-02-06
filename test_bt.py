import sudoku_bt, time

def test1():
        
    sudoku_bt.count = 0
    sudoku_bt.N=6
    map=[
        [0,1,0,0,0,5], 
        [0,6,0,0,0,2],
        [0,0,0,1,0,4], 
        [0,0,0,2,3,0],
        [4,2,0,0,0,0],
        [0,0,6,0,2,0], 
        ]

    sudoku_bt.display(map)
    t0=time.time()
    r=sudoku_bt.BT(map, 0, 0)
    t1=time.time()
    
    if r:
        sudoku_bt.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_bt.count))
    else:
        print("no solutions.")

def test2():
   
    sudoku_bt.count = 0
    sudoku_bt.N=8
    map=[
        [0,0,0,0,0,8,0,6], 
        [0,4,0,5,0,0,7,0],
        [3,0,2,0,7,0,0,0],
        [0,6,0,8,0,3,0,0],
        [0,0,4,0,0,0,1,0],
        [0,1,0,6,0,0,0,0],
        [8,0,0,0,5,0,4,0],
        [0,0,0,0,0,7,8,0],
        ]
    sudoku_bt.display(map)
    t0=time.time()
    r=sudoku_bt.BT(map, 0, 0)
    t1=time.time()
    
    if r:
        sudoku_bt.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_bt.count))
    else:
        print("no solutions.")
        

def test3():
    sudoku_bt.count = 0
    sudoku_bt.N=9
    map=[
        [0,0,0,8,4,0,6,5,0],
        [0,8,0,0,0,0,0,0,9],
        [0,0,0,0,0,5,2,0,1],
        [0,3,4,0,7,0,5,0,6],
        [0,6,0,2,5,1,0,3,0],
        [5,0,9,0,6,0,7,2,0],
        [1,0,0,5,0,0,0,0,0],
        [6,0,0,0,0,0,0,4,0],
        [0,5,0,0,8,0,0,0,0],
    ]

    sudoku_bt.display(map)
    t0=time.time()
    r=sudoku_bt.BT(map, 0, 0)
    t1=time.time()
    
    if r:
        sudoku_bt.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_bt.count))
    else:
        print("no solutions.")

def test4():
    sudoku_bt.count = 0
    sudoku_bt.N=10
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

    sudoku_bt.display(map)
    t0=time.time()
    r=sudoku_bt.BT(map, 0, 0)
    t1=time.time()
    
    if r:
        sudoku_bt.display(map)
        print("time: %.3fs" %(t1-t0))
        print("# of recurrence: %d" %(sudoku_bt.count))
    else:
        print("no solutions.")

        
if __name__=='__main__':
    test1()
    test2()
    test3()
    test4()
