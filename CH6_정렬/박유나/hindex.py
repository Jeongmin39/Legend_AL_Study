def solution(citations):
    h = len(citations) 
    citations.sort()
    for i in citations:
        if i >= h:
            return h
        h=h-1
    return 0