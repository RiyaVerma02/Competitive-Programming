import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def reverse(A,s,e):
    n=len(A)
    while(s<e):
        A[s]=A[s]+A[e]
        A[e]=A[s]-A[e]
        A[s]=A[s]-A[e]
        s+=1
        e-=1
    return A    


def rotate(A,elem):
    K=[]
    for val in A:
        K.append(val)
    n=len(K)
    elem = n - elem
    K=reverse(K,0,n-1)
    K=reverse(K,0,elem-1)
    K=reverse(K,elem,n-1)
    return K


def solve(A,B):
    ans=[]
    for elem in B:
        arr = rotate(A,elem)
        ans.append(arr)
    return ans

while t > 0:
    t -= 1
    arr=list(map(int,input().split()))
    rotations=list(map(int,input().split()))
    print(solve(arr,rotations))