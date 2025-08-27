import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(arr): 
    n=len(arr)
    for i in range(1,n):
        arr[i]+=arr[i-1]
    return arr    


    

while t > 0:
    arr = list(map(int,input().split()))
    print(solve(arr))
    t -= 1
