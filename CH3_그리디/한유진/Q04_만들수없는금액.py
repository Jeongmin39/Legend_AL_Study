N = int(input())
coins = sorted(list(map(int, input().split())))
minResult = 1

for i in range(N):
    if minResult < coins[i]:
        break
    minResult += coins[i]

print(minResult)