import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A,B,C):
    n=len(A)
    sum_v=0
    for i in range(B):
        sum_v+=A[i]
    if sum_v==C:
        return 1
    e=B
    s=1
    while(e<n):
        sum_v+=A[e]-A[s-1]
        s+=1
        e+=1
        if sum_v==C:
            return 1      
    return 0

while t > 0:
    t -= 1
    arr=list(map(int,input().split()))
    b=int(input())
    c=int(input())
    print(solve(arr,b,c))
