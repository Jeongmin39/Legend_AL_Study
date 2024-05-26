N , C = map(int, input().split())
seq = []

for _ in range(N):
    seq.append(int(input()))
seq.sort()

firstGap = seq[1] - seq[0]
lastGap = seq[-1] - seq[0]
maxGap = 0

while(firstGap <= lastGap) :
    mid = (firstGap + lastGap) // 2
    
    curInstalledHouse = seq[0]
    installCnt = 1
    
    for i in range(1, N):
        if seq[i] >= mid + curInstalledHouse:
            curInstalledHouse = seq[i]
            installCnt += 1
    
    if installCnt >= C:
        firstGap = firstGap + 1
        maxGap = mid
    else:
        lastGap = lastGap - 1
        
print(maxGap)