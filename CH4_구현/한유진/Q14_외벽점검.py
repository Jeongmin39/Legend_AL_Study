import itertools

def solution(n, weak, dist):
    weakPoints = [n*i + j for i in range(2) for j in weak]
    distComb = list(itertools.permutations(dist))
    
    numP = 1e9
    for dist in distComb:
        temp = 1e9
        for i in range(len(weakPoints) - 1):
            
            
            
    
    answer = 0
    return answer