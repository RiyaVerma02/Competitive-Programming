import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A):
    n=len(A)
    idx_zero=[]
    count=0
    ans=0
    for i in range(n):
        if(A[i]==0):
            idx_zero.append(i)
    m=len(idx_zero)
    if m==0 or m==1:
        return n
    for i in range(m):
        if i==0: 
            count=idx_zero[i+1]                                   
        elif i== m-1:
            if (idx_zero[i]!=(n-1)):           
                count=(n-1)-(idx_zero[i-1]+1)+1
            else:                  
                count=idx_zero[i]-(idx_zero[i-1]+1)+1
        else:         
            count=idx_zero[i+1]-idx_zero[i-1]-1           
        if (ans<count):
            ans=count
    return ans

while t > 0:
    t -= 1
    arr=list(map(int,input().split()))
    print(solve(arr))