import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A,B):
    n=len(A)
    ps=[0]*n
    ps[0]=A[0]
    for i in range(1,n):
        ps[i]=ps[i-1]+A[i]  
 
    max_sum=float("-inf")      
    for i in range(B+1):
        l=i
        r=B-l
        sum_l=0
        sum_r=ps[n-1]
        if l!=0:    
            sum_l=ps[l-1]
        if (n-r-1)>=0:    
            sum_r-=ps[n-r-1]  
        max_sum=max(sum_r+sum_l,max_sum)  
    return max_sum       
        





while t > 0:
    t -= 1
    arr=list(map(int,input().split()))
    b=int(input())
    print(solve(arr,b))
