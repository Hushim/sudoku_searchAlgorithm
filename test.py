import test_dfs, test_bt, test_iddfs, Sudoku_BFS_test

if __name__=='__main__':
    print("****** BFS ******")
    print("*********** DFS 6*6 *********")
    Sudoku_BFS_test.test1()
    Sudoku_BFS_test.test2()
    print("********* DFS 9*9 ************")
    Sudoku_BFS_test.test3()

    
    print("****** DFS ******")
    print("*********** DFS 6*6 *********")
    test_dfs.test1()
    print("*********** DFS 8*8 *********")
    test_dfs.test2()
    print("********* DFS 9*9 ************")
    test_dfs.test3()
    print("********* DFS 10*10 ************")
    test_dfs.test4()


    print("\n*********** Backtracking search ********")
    print("\n********* Backtracking search 6*6 ********")
    test_bt.test1()
    print("\n********* Backtracking search 8*8 ********")
    test_bt.test2()
    print("\n********* Backtracking search 9*9 ********")
    test_bt.test3()
    print("\n********* Backtracking search 10*10 ********")
    test_bt.test4()
    
    
    print("****** Iterative DFS ******")
    print("\n****** Itearative deepning search 6*6 *********")
    test_iddfs.test1()
    print("\n****** Itearative deepning search 8*8*********")
    test_iddfs.test2()
    print("\n****** Itearative deepning search 9*9*********")
    test_iddfs.test3()
    print("\n****** Itearative deepning search 10*10*********")
    test_iddfs.test4()
   

   
   


    
