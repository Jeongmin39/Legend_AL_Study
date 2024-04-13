def solution(N, stages):
    failure_rate = []
    totalPlayer = len(stages)
    
    for i in range(1, N+1):
        if i not in stages:
            failure_rate.append((i, 0))
            continue
        failure_rate.append((i, stages.count(i)/totalPlayer))
        totalPlayer -= stages.count(i)
    
    failure_rate = sorted(failure_rate, key=lambda x: -x[1])
    answer = [x for x, _ in failure_rate]
            
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))