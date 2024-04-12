#q24 안테나
N=int(input())
houselist=list(map(int,input().split()))
houselist.sort()
mid=(N-1)//2
print(houselist[mid])
