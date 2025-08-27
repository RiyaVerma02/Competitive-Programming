import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A):
    n,m=len(A),len(A[0])
    row_set=set()
    col_set=set()
    for i in range(n):
        for j in range(m):
            if (A[i][j]==0):
                row_set.add(i)
                col_set.add(j)
    for row in row_set:
        for j in range(m):
            A[row][j]=0
    for col in col_set:        
        for i in range(n):
            A[i][col]=0
    return A           
        




while t > 0:
    t -= 1
    rows=int(input())
    mat=[]
    for i in range(rows):
        arr = list(map(int,input().split()))
        mat.append(arr)
    print(solve(mat))

