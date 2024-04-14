import heapq

def sortCards(num_cards):
    cardPack = []
    for _ in range(num_cards):
        heapq.heappush(cardPack, int(input()))
    
    result = 0
    while len(cardPack) != 1:
        sum = heapq.heappop(cardPack) + heapq.heappop(cardPack)
        result += sum
        heapq.heappush(cardPack, sum)

    print(result)

N = int(input())
sortCards(N)