from bisect import bisect_left, bisect_right

word_list = [[] for _ in range(10001)]
word_list_reversed = [[] for _ in range(10001)]

def lyric_search(n_word_list, lower_bound, upper_bound):
    lower_index = bisect_left(n_word_list, lower_bound)
    upper_index = bisect_right(n_word_list, upper_bound)
    
    return upper_index - lower_index

def solution(words, queries):
    answer = []
    
    for word in words:
        word_list[len(word)].append(word)
        word_list_reversed[len(word)].append(word[::-1])
    
    for i in range(10001):
        word_list[i].sort()
        word_list_reversed[i].sort()
        
    includeCnt = 0
    for query in queries:
        if query[0] != '?': # '?'가 접미사로 주어질 때, fro???
            includeCnt = lyric_search(word_list[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:               # '?'가 접두사로 주어질 때, ????en
            includeCnt = lyric_search(word_list_reversed[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(includeCnt)
        
    return answer