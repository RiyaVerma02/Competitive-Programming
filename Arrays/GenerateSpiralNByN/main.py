import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A):
    arr=[]
    for i in range(A):
        arr.append([0]*A)
    i=0
    j=0
    count=0
    while(A>1):
        for k in range(A-1):
            count=count+1
            arr[i][j]=count
            j+=1
        for k in range(A-1):
            count=count+1
            arr[i][j]=count
            i+=1  
        for k in range(A-1):
            count=count+1
            arr[i][j]=count
            j-=1
        for k in range(A-1):
            count=count+1
            arr[i][j]=count 
            i-=1      
        i+=1
        j+=1
        A=A-2     
    if A==1:     
        arr[i][j]=count+1     
    return arr

while t > 0:
    t -= 1
    A=int(input())
    print(solve(A))