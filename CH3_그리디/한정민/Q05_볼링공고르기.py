N, M = map(int, input().split())
weight = list(map(int, input().split()))
count = 0

for i in range (len(weight) - 1):
    for j in range(i+1, len(weight)):
        if (weight[i] != weight[j]):
            count += 1

print(count)
