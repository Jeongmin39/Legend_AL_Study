from bisect import bisect_left, bisect_right
N, x = map(int, input().split())
mylist = list(map(int, input().split()))
cnt = bisect_right(mylist, x) - bisect_left(mylist, x)
if cnt == 0:
    print(-1)
else:
    print(cnt)