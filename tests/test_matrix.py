import sys
sys.path.append('src')
from matrix import Matrix

tests_1 = True 
if tests_1 == True: 
  print('testing matrix')
  A = Matrix([[1,3],[2,4]])
  print(A.elements)
  assert A.elements == [[1,3],[2,4]], 'Answer is supposed to be [[1,3],[2,4]]'
  print('Passed')

  B = A.copy()
  A = 'resetting A to a string'
  print('Testing method copy')
  print(B.elements)
  assert B.elements == [[1,3],[2,4]], 'Answer is supposed to be [[1,3],[2,4]]'
  print('Passed')

  print('Testing method add')
  C = Matrix([[1,0],[2,-1]])
  D = B.add(C)
  print(D.elements)
  assert D.elements == [[2,3],[4,3]], 'Answer is supposed to be [[2,3],[4,3]]'
  print('Passed')
  #[[2,3],[4,3]]

  print('Testing method subtract')
  E = B.subtract(C)
  print(E.elements)
  assert E.elements == [[0,3],[0,5]], 'Answer is supposed to be [[0,3],[0,5]]'
  print('Passed')
  #[[0,3],[0,5]]

  print('Testing method scalar_multiply')
  F = B.scalar_multiply(2)
  print(F.elements)
  assert F.elements == [[2,6],[4,8]], 'Answer is supposed to be [[2,6],[4,8]]'
  print('Passed')
  #[[2,6],[4,8]]
  
  G = B.matrix_multiply(C)
  print('Testing method matrix_multiply')
  print(G.elements)
  assert G.elements == [[7,-3],[10,-4]], 'Answer is supposed  to be [[7,-3],[10,-4]]'
  print('Passed')
  #[[7,-3],[10,-4]]

tests_2 = True
if tests_2 == True:
  A = Matrix([[1,0,2,0,3],
                [0,4,0,5,0],
                [6,0,7,0,8],
                [-1,-2,-3,-4,-5]])
  print(A.num_rows, A.num_cols)
  (4, 5)
  
  print('testing transpose')
  A_t = A.transpose()
  print(A_t.elements)
  assert A_t.elements == [[ 1,  0,  6, -1],[ 0,  4,  0, -2],[ 2,  0,  7, -3],[ 0,  5,  0, -4],[ 3,  0,  8, -5]],"Correct answer was [[ 1,  0,  6, -1],[ 0,  4,  0, -2],[ 2,  0,  7, -3],[ 0,  5,  0, -4],[ 3,  0,  8, -5]]"
  print('Passed')

  print('testing matrix_multiply')
  B = A_t.matrix_multiply(A)
  print(B.elements)
  assert B.elements ==[[38, 2, 47, 4, 56], [2, 20, 6, 28, 10],[47,6,62,12,77], [4, 28, 12, 41, 20], [56, 10, 77, 20,98]]
  print('passed')

  print('testing scalar_multiply')
  C = B.scalar_multiply(0.1)
  print(C.elements)
  assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6],
  [ .2, 2.0,  .6, 2.8, 1.0],
  [4.7,  .6, 6.2, 1.2, 7.7],
  [ .4, 2.8, 1.2, 4.1, 2.0],
  [5.6, 1.0, 7.7, 2.0, 9.8]]
  print('passed')

  print('testing subtract')
  D = B.subtract(C)
  print(D.elements)
  assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4],
  [ 1.8, 18. ,  5.4, 25.2,  9. ],
  [42.3,  5.4, 55.8, 10.8, 69.3],
  [ 3.6, 25.2, 10.8, 36.9, 18. ],
  [50.4,  9. , 69.3, 18. , 88.2]]
  print('passed')
  
  print('testing add')
  E = D.add(C)
  print(E.elements)
  assert E.elements == [[38,  2, 47,  4, 56],
  [ 2, 20,  6, 28, 10],
  [47,  6, 62, 12, 77],
  [ 4, 28, 12, 41, 20],
  [56, 10, 77, 20, 98]]
  print('passed')

  print('testing is_equal') 
  print((E.is_equal(B), E.is_equal(C)))
  assert (E.is_equal(B), E.is_equal(C)) == (True, False)
  print('passed')

test__3 = True
if test__3 == True:
  A = Matrix( [[0, 1, 2],
              [3, 6, 9],
              [2, 6, 8]])
  print('testing get_pivot_row')
  print(A.get_pivot_row(0))
  assert A.get_pivot_row(0) == 1, 'Answer wasnt 1'
  print('passed')
  1
  print('testing swap_rows')
  A.swap_rows(0,1)
  print(A.elements)
  assert A.elements == [[3, 6, 9],
  [0, 1, 2],
  [2, 6, 8]], 'Answer wasnt [[3, 6, 9],[0, 1, 2],[2, 6, 8]]'
  
  print('testing normalize_row')
  A.normalize_row(0)
  print(A.elements)
  assert A.elements == [[1, 2, 3],
  [0, 1, 2],
  [2, 6, 8]], 'Answer wasnt [[1, 2, 3],[0, 1, 2],[2, 6, 8]]'
  print('passed')

  print('testing clear_below')
  A.clear_below(0)
  print(A.elements)
  assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]]
  print('passed')

  print('testing get_pivot_row')
  print(A.get_pivot_row(1))
  assert A.get_pivot_row(1) == 1, 'Answer wasnt 1'
  print('passed')
  1
  print('testing normalize_row')
  A.normalize_row(1)
  print(A.elements)
  assert A.elements == [[1, 2, 3],
  [0, 1, 2],
  [0, 2, 2]]
  print ('passed')
  
  print('testing clear_below')
  A.clear_below(1)
  print(A.elements)
  assert A.elements == [[1, 2, 3],[0, 1, 2],[0, 0, -2]]
  print('passed')

  
  print('testing get_pivot_row')
  print(A.get_pivot_row(2))
  assert A.get_pivot_row(2) == 2, 'Answer wasnt 2'
  print('passed')
  
  print('testing normalize_row')
  A.normalize_row(2)
  print(A.elements)
  assert A.elements == [[1, 2, 3],
  [0, 1, 2],
  [0, 0, 1]]
  print('passed')
  
  print('testing clear_above')
  A.clear_above(2)
  print(A.elements)
  assert A.elements == [[1, 2, 0],[0, 1, 0],[0, 0, 1]]
  print('Passed')

  print('testing clear_above')
  A.clear_above(1)
  print(A.elements)
  assert A.elements == [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
  print('passed')
