'''
not that efficient -- use bitwise operators?
'''

def flipAndInvertImage(A):
    for i in range(len(A)):
        # reverses each list in-place (overwrites)
        A[i].reverse()
        # invert the value of every list
        for j in range(len(A[i])):
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1

    return A

    

A = [[1,1,0],[1,0,1],[0,0,0]]

flipAndInvertImage(A)