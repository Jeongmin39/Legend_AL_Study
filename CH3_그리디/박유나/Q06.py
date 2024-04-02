import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    #힙을 이용해서 작은거 빼내기
    heapp=[]
    for i in range(len(food_times)):
        heapq.heappush(heapp,(food_times[i],i+1))
    total=0 
    p=0
    l=len(food_times)
    #음식 다먹는데 걸리는게 k이하로 남은 경우
    while total+(heapp[0][0]-p)*l<=k:  
        now=heapq.heappop(heapp)[0]
        total=total+(now-p)*l
        p=now
        l=l-1
    #이제 번호순으로 정리후 반환
    a = sorted(heapp, key=lambda x: x[1])
    return a[(k-total)%l][1]