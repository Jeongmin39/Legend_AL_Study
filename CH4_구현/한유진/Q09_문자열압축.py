def solution(s):
    minLength = len(s)
    
    for unit in range(1, len(s) // 2 + 1):
        prev = s[0: unit]
        cnt = 0
        answer = ""
        
        for j in range(unit, len(s), unit):
            if prev == s[j:j + unit]:
                cnt += 1
            else:
                answer += str(cnt+1)+prev if cnt !=0 else prev
                cnt = 0
            prev = s[j:j + unit]
            
        answer += str(cnt+1)+prev if cnt !=0 else prev
        if minLength > len(answer):
            minLength = len(answer)
            
    return minLength

compressedLength = solution("abcabcdede")
print(compressedLength)