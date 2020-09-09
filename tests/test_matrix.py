import sys
sys.path.append('src')
from matrix import Matrix
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


C = Matrix([[1,0],[2,-1]])
print(C.elements)
D = B.add(C)

print('Testing method add')
print(D.elements)
assert D.elements == [[2,3],[4,3]], 'Answer is supposed to be [[2,3],[4,3]]'
print('Passed')
#[[2,3],[4,3]]

E = B.subtract(C)
print('Testing method subtract')
print(E.elements)
assert E.elements == [[0,3],[0,5]], 'Answer is supposed to be [[0,3],[0,5]]'
print('Passed')
#[[0,3],[0,5]]

F = B.scalar_multiply(2)
print('Testing method subtract')
print(F.elements)
assert F.elements == [[2,6],[4,8]], 'Answer is supposed to be [[2,6],[4,8]]'
print('Passed')
#[[2,6],[4,8]]

G = B.matrix_multiply(C)
print('Testing method subtract')
print(G.elements)
assert G.elements == [[7,-3],[10,-4]], 'Answer is supposed to be [[7,-3],[10,-4]]'
print('Passed')
#[[7,-3],[10,-4]]