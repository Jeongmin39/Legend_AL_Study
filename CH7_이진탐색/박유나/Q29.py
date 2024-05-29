import sys
from bisect import bisect_left

N, C = map(int, sys.stdin.readline().rstrip().split())
mylist = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

mylist.sort()
start=1
end=mylist[-1]-mylist[0]
answer=0

while start<=end:
    mid=(end+start)//2
    left=0
    cnt=0
    while left<N:
       cnt=cnt+1
       left=bisect_left(mylist,mylist[left]+mid)
    if cnt>=C:
        start=mid+1
        answer=mid
    else:
        end=mid-1
print(answer)