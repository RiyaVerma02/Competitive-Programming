import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(arr):
    n=len(arr)
    rows=2*n-1
    cols=n
    idx=0
    ans=[[0 for _ in range(cols)] for _ in range(rows)]
    for j in range(n):
        x=0
        y=j
        temp=[]
        while(x<n and y>=0):
            temp.append(arr[x][y])
            x+=1
            y-=1
        for k in range(len(temp)):
            ans[idx][k]=temp[k]
        idx+=1

    for i in range(1,n):
        x=i
        y=n-1
        temp=[]
        while(x<n and y>=0):
            temp.append(arr[x][y])     
            x+=1
            y-=1
        for k in range(len(temp)):
            ans[idx][k]=temp[k]
        idx+=1       
    return ans   
            
            




while t > 0:
    t -= 1
    row = int(input())
    mat = []
    for i in range(row):
        arr = list(map(int,input().split()))
        mat.append(arr)
           
    print(solve(mat))    
    
