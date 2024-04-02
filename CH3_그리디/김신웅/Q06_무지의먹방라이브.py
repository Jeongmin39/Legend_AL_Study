def solution(food_times, k):
    answer = 0
    cnt = 0 
    size = len(food_times)
    initial = 0
    #인덱스 제어할 변수
    i = 0
    while cnt < k:
        #for문 끝나는 시점 알기위해 cnt 계산
        cnt += 1
        #인덱스를 새로 계산
        idx = i % size
        #0이 아닐때까지 뒤로 인덱스 넘기기
        while True:
            if food_times[idx] != 0:
                break
            
            if food_times[idx] == 0:
                i += 1
                idx = i % size
            
            #수행중에 음식이 다 0이면 -1을 return
            if sum(food_times) <= 0:
                return -1
            
        #0이 아니라면 음식개수 1개 줄이기
        if food_times[idx] != 0:
            food_times[idx] = food_times[idx] - 1
        
        #마지막엔 1씩 증가
        i+=1
        #print(food_times)
    #print(i % size)
    
    ##다 0 이면 return -1
    if sum(food_times) <= 0:
        return -1
    
    while True:
        next_idx = i % size
        if food_times[next_idx] == 0 :
            i +=1
        elif food_times[next_idx] != 0 :
            answer = next_idx + 1
            break
    
    return answer
