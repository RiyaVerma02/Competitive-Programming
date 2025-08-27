import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def reverse(arr,s,e):
    while s<=e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1


def solve(arr,k):
    arr = arr[::-1]
    n = len(arr)
    k = k%n;
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    return arr

while t > 0:
    arr = list(map(int,input().split()))
    k = int(input())
    print(solve(arr,k))
    t -= 1
