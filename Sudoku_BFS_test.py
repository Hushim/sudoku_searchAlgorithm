import BFSsudoku, time

def test1():
    BFSsudoku.NotesNum = 0
    BFSsudoku.N = 6
    initState =[
        [2,0,0,0,4,0], 
        [5,6,0,0,0,0],
        [3,0,2,6,5,4], 
        [0,4,0,2,0,3],
        [4,0,0,0,6,5],
        [1,5,6,0,0,0], 
        ]
    
    BFSsudoku.display(initState)
    pro = BFSsudoku.Problem(initState)
    t0=time.time()
    BFSsudoku.result = BFSsudoku.breadth_first_search(pro)
    t1=time.time()
    
    if(BFSsudoku.result == None):
        print("no result")
    else:
        print("the result:")
        for i in range (BFSsudoku.N):
            for j in range(BFSsudoku.N):
                print(BFSsudoku.result.state[i][j],end = " ")
            print()
    print("time: %.7fs" %(t1-t0))
    print("the total child notes searched:%d"%BFSsudoku.NotesNum)

def test2():
    BFSsudoku.NotesNum = 0
    BFSsudoku.N = 6
    initState =[
        [0,1,0,0,0,5], 
        [0,6,0,0,0,2],
        [0,0,0,1,0,4], 
        [0,0,0,2,3,0],
        [4,2,0,0,0,0],
        [0,0,6,0,2,0], 
        ]

     
    BFSsudoku.display(initState)
    pro = BFSsudoku.Problem(initState)
    t0=time.time()
    BFSsudoku.result = BFSsudoku.breadth_first_search(pro)
    t1=time.time()

    if(BFSsudoku.result == None):
        print("no result")
    else:
        print("the result:")
        for i in range (BFSsudoku.N):
            for j in range(BFSsudoku.N):
                print(BFSsudoku.result.state[i][j],end = " ")
            print()
    print("time: %.7fs" %(t1-t0))
    print("the total child notes searched:%d"%BFSsudoku.NotesNum)

def test3():
    BFSsudoku.NotesNum = 0
    BFSsudoku.N = 9
    initState =[
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

     
    BFSsudoku.display(initState)
    pro = BFSsudoku.Problem(initState)
    t0=time.time()
    BFSsudoku.result = BFSsudoku.breadth_first_search(pro)
    t1=time.time()

    if(BFSsudoku.result == None):
        print("no result")
    else:
        print("the result:")
        for i in range (BFSsudoku.N):
            for j in range(BFSsudoku.N):
                print(BFSsudoku.result.state[i][j],end = " ")
            print()
    print("time: %.7fs" %(t1-t0))
    print("the total child notes searched:%d"%BFSsudoku.NotesNum)


if __name__=='__main__':
    test1()
    test2()
    test3()
