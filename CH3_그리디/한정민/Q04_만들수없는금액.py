count = int(input())
coins = list(map(int, input().split()))
coins.sort()
result = 1

for i in range(count):
    if result < coins[i]:
        break
    result += coins[i]

print(result)
