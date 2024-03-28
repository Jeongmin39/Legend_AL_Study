#모험가 길드
num=0
cnt=0
N=int(input())
fear=list(map(int,input().split()))
fear.sort()
for element in fear:
    num=num+1
    if num>=element:
        cnt=cnt+1
        num=0
print(cnt)




