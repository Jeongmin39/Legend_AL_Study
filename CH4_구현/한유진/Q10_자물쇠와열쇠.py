def rotate90clockwise(key):
    numrows = len(key)
    rotatedKey = [[0 for _ in range(numrows)] for _ in range(numrows)]
    print(rotatedKey)
    
    for i in range(numrows):
        for j in range(numrows):
            rotatedKey[j][numrows -1 - i] = key[i][j]
    return rotatedKey

def checkOpen(lock, N):
    for i in range(len(lock) // 3, len(lock) // 3 + N):
        for j in range(len(lock) // 3, len(lock) // 3 + N):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    expandedLock = [[0 for _ in range(N * 3)] for _ in range(N * 3)]
    
    for i in range(N):
        for j in range(N):
            expandedLock[i + N][j + N] = lock[i][j]
    
    for _ in range(4):
        key = rotate90clockwise(key)
        
        for i in range(N * 2):
            for j in range(N * 2):
                for m in range(M):
                    for n in range(M):
                        expandedLock[i + m][j + n] += key[m][n]
                if checkOpen(expandedLock, N) :
                    return True
                for m in range(M):
                    for n in range(M):
                        expandedLock[i + m][j + n] -= key[m][n]
    return False