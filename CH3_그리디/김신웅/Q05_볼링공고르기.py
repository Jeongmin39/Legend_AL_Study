a, b = map(int, input().split())
ball_list = list(map(int,input().split()))
cnt = 0
for i in range(a):
    for j in range(i+1,a):
        if ball_list[i] != ball_list[j]:
            cnt +=1

print(cnt)
