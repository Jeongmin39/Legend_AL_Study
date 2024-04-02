def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1
    
    passed_time = 0
    while True:
        for i in range(len(food_times)):
            required_time = food_times[i]
            passed_time += required_time
            
            if passed_time >= k:
                remaining_time = passed_time - required_time
                remainder = k - remaining_time
                answer = (i + 1 + remainder) % len(food_times)
                return answer if answer != 0 else len(food_times)
            food_times[i] = 0
          
    return answer
