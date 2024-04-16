'''
def solution(citations):
    answer = 0
    result = []
    # 내림차순 정렬
    citations.sort(reverse = True)
    for citation in citations:
        left_list = citations[:citations.index(citation)+1]
        if len(left_list) >= citation:
            result.append(citation)
    answer = max(result)
    return answer
'''

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            answer = i + 1
        else:
            break
    return answer