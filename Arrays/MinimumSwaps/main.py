import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A,B):
    n=len(A)
    count=0
    for elem in A:
        if elem<=B:
            count+=1
    if count==0 or count==1:
        return 0
    bad=0
    for s in range(count):
        if A[s]>B:
            bad+=1
    s=1 
    e=count
    ans=bad
    while(e<n):
        if A[s-1]>B:
            bad-=1
        if A[e]>B:
            bad+=1    
        if(ans>bad):
            ans=bad
        s+=1
        e+=1    

    return ans

while t > 0:
    t -= 1
    arr = list(map(int,input().split()))
    b=int(input())
    print(solve(arr,b))

