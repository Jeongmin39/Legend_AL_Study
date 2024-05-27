from bisect import bisect_left
answer=-1
N=int(input())
mylist = list(map(int, input().split()))
for i in range(N):
    if mylist[i]==bisect_left(mylist,mylist[i]):
        answer=mylist[i]
        break;
    
print(answer)