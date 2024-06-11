N = int(input())
power = list(map(int, input().split()))

# dp[i] == i번째 병사를 마지막으로 하는 가장 긴 내림차순 부분 수열의 길이
dp = [1] * (N+1)
for i in range(1, N):
    for j in range(0, i):
        if power[j] > power[i]:
            # 내림차순 조건 만족하면 dp값 갱신
            dp[i] = max(dp[i], dp[j] + 1)
            
print(N-max(dp))