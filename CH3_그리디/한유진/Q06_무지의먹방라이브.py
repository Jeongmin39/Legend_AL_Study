'''
# 처음 코드 : 정확도 통과, 효율성 꽝...
# for문 2번이나 사용해서...

def solution(food_times, k):
    answer = 0
    foodCnt = len(food_times)

    if sum(food_times) <= k:
        return -1
    
    for i in range(k):
        for j in range(foodCnt):
            if food_times[(answer + j) % foodCnt] != 0:
                food_times[(answer + j) % foodCnt] -= 1
                answer = (answer + j + 1) % foodCnt
                break

    for i in range(foodCnt):
        if food_times[(answer + i) % foodCnt] != 0:
            return (answer + i) % foodCnt + 1
'''

import heapq

def solution(food_times, k):
    foodHeap = []

    if sum(food_times) <= k:
        return -1
    
    for i in range(len(food_times)):
        heapq.heappush(foodHeap, (food_times[i], i + 1))
    
    sum_times = 0
    prev_time = 0
    length = len(food_times)
    while sum_times + ((foodHeap[0][0] - prev_time) * length) <= k:
        now = heapq.heappop(foodHeap)[0]
        print("now: ", now)
        sum_times += (now - prev_time) * length
        print("sum_times: ", sum_times)
        length -= 1
        prev_time = now
    
    result = sorted(foodHeap, key=lambda x:x[1] )
    
    return result[(k - sum_times) % length][1]

result = solution([3,2,2], 5)
print(result)