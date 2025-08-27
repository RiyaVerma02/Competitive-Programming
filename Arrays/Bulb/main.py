import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(A):
    parity=0
    for elem in A:
        if(elem ^ (parity%2)==0):
            parity+=1
    return parity
while t > 0:
    t -= 1
    arr= list(map(int,input().split()))
    print(solve(arr))
