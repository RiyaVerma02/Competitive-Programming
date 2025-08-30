import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())


def maxSubarray(arr,k):
	#Brute Force
    n=len(arr)
    max_sum=float("-inf")
    for s in range(n):
        sum_v=0
        e=k+s-1
        if(e>=n):
            break
        for j in range(s,e+1):
            sum_v+=arr[j]
        max_sum=max(max_sum,sum_v)
    return max_sum
def maxSubarray2(arr,k): #Brute force beautified
    n,max_sum,s=len(arr),float("-inf"),0
    while k+s-1<n:
        sum_v=0
        for j in range(s,k+s):
            sum_v+=arr[j]
        max_sum=max(max_sum,sum_v)
    return max_sum
def maxSubarray3(arr,k): #Prefix Sum
    ps=[0]*len(arr)
    ps[0]=arr[0]
    max_sum=float("-inf")
    for i in range(1,len(arr)):
        ps[i] = ps[i-1]+arr[i]
    s=0
    e=k-1    
    while(e<len(arr)):
        curr_sum = ps[e]
        if s!=0:
            curr_sum -= ps[s-1]
        max_sum=max(max_sum,curr_sum)
        s+=1
        e+=1  
    return max_sum  

def maxSubarray4(arr,k): #Sliding Window
    sum_v=0
    for i in range(k):
        sum_v+=arr[i]
    max_sum=sum_v
    s,e=1,k
    while(e<len(arr)):
        sum_v=sum_v-arr[s-1]+arr[e]
        s+=1
        e+=1    
        max_sum=max(sum_v,max_sum)
    return max_sum    

while t > 0:
    arr = list(map(int,input().split()))
    k = int(input())
    print(maxSubarray4(arr,k))
    t -= 1

