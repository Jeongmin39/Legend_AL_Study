'''
효율성 테스트 1~3 실패
def solution(words, queries):

    wordLen = len(words)
    queryLen = len(queries)
    answer = [0] * queryLen

    for i in range(queryLen):
        query = queries[i]
        # ? 제거 전 원래 query 길이
        beforeLen = len(query)
        head = False

        # ? 위치 접두사이면 True / 접미사이면 False
        if query[0] == '?':
            head = True

        query = query.replace("?", "")
        # ? 제거 후 query 길이
        afterLen = len(query)
        count = 0
        for j in range(wordLen):
            word = words[j]
            if len(word) != beforeLen:
                continue
            if head:
                word = word[-afterLen:]
            else:
                word = word[:afterLen]
            if query == word:
                count += 1
        answer[i] = count

    return answer
'''

def solution(words, queries):
    origin_map = {}
    reverse_map = {}

    for word in words:
        length = len(word)

        if length not in origin_map:
            origin_map[length] = []
        if length not in reverse_map:
            reverse_map[length] = []

        origin_map[length].append(word)
        reverse_map[length].append(word[::-1])

    for length in origin_map:
        origin_map[length].sort()
        reverse_map[length].sort()

    answer = []
    for query in queries:
        if query[0] == '?':
            array = reverse_map.get(len(query), [])
            query = query[::-1]
        else:
            array = origin_map.get(len(query), [])

        if not array:
            answer.append(0)
        else:
            answer.append(lower_bound(array, query.replace('?', 'z')) - lower_bound(array, query.replace('?', 'a')))

    return answer

def lower_bound(array, string):
    start, end = 0, len(array)

    while start < end:
        mid = (start + end) // 2
        if string <= array[mid]:
            end = mid
        else:
            start = mid + 1
    return start
