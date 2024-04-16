'''
https://school.programmers.co.kr/learn/courses/30/lessons/42747

[정렬] H-index

def solution(citations):
    citations.sort(key= lambda x: x)
    
    h_index = 0
    num = 0
    length = len(citations)
    for i, citation in enumerate(citations):
        if citation <= length:
            h_index = citation
        
        if length != 1 and num != length -1:
            if citations[i+1] != citation:
                length -= (num +1)
                num = 0
            else:
                num += 1
        
    return h_index
'''
            
def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return (len(citations))

print(solution([0, 0, 1, 1, 2]))