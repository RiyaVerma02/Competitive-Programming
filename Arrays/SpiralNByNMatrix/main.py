import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A):
    n,m=len(A),len(A[0])

    i,j=0,0
    while(n>1):

        for k in range(n-1):
            print(A[i][j])
            j+=1
        for k in range(n-1):
            print(A[i][j])
            i+=1
        for k in range(n-1):
            print(A[i][j])
            j-=1
        for k in range(n-1): 
            print(A[i][j])
            i-=1          
        i+=1
        j+=1
        n-=2
    if (n==1):   #In while loop we are printing for n-1 elements, in loop, 1-1=0, so zero elements would have been printed
        print(A[i][j])

    ''' Boarder Clockwise
    for j in range(m):
        print(A[0][j])
    for i in range(1,n):
        print(A[i][m-1])
    for j in range(m-2,-1,-1):
        print(A[n-1][j])
    for i in range(n-2,0,-1):
        print(A[i][0])        
    '''

while t > 0:
    t -= 1
    rows=int(input())
    mat=[]
    for i in range(rows):
        mat.append(list(map(int,input().split())))
    solve(mat) 


