import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def minSwaps(arr,b):                 
    count=0
    for i in range(len(arr)):
        if arr[i]<=b:
            count+=1
    #print(count)        
    min_swap=float("inf")
    for s in range(len(arr)-count+1):
        e=count+s-1
        swap=0
        for i in range(s,e+1):
            if arr[i]>b:
                swap+=1   
        #print(swap)         
        min_swap=min(swap,min_swap) 
    return min_swap      

def minSwaps2(arr,b):
    count=0
    swap=0
    for i in range(len(arr)):
        if arr[i]<=b:
            count+=1
    for i in range(count):
            if(arr[i]>b):
                swap+=1
    min_swap=swap            
    s=1
    while(count+s-1<len(arr)):
        if(arr[s-1]>b):
            swap-=1
        if (arr[count+s-1]>b):
            swap+=1
        min_swap=min(swap,min_swap)
        s+=1 
    return min_swap



                


while t > 0:
    t -= 1
    arr = list(map(int,input().split()))
    b=int(input())
    print(minSwaps2(arr,b))
