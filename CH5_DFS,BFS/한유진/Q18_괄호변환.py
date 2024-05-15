def balanced_string(p):
    count = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        else:
            count-=1
        if count == 0:
            return i
    
def correct_string(p):
    count = 0
    
    for i in p:
        if i == '(':
            count+=1
        else:
            if count == 0:
                return False
            count-=1
            
def solution(p):
    answer=""
    
    if p == "": # 1. 입력이 빈 문자열이면 빈 문자열 반환
        return answer
    
    balanced_Index = balanced_string(p)
    
    # 2. 문자열을 두 개의 균형잡힌 괄호 문자열 u,v로 나눔
    u = p[:balanced_Index+1]
    v = p[balanced_Index+1:]
    
    if correct_string(u):
        # 3-1. u가 올바른 문자열이면 v에 대해 1단계부터 진행
        answer = u + solution(v)
    else: # 4. u가 올바른 문자열이 아니면
        # 4-1. 빈 문자열에 '(' 붙임
        # 4-2. v에 대해 1단계부터 재귀적 진행해 문자열에 붙임
        # 4-3. ')'를 붙임
        answer = "(" + solution(v) + ")"
        
        # 4-4. u의 처움과 마지막 문자 제거 후 나머지 문자열을 괄호 방향 뒤집어 뒤에 붙임
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
                
        answer += "".join(u)
    
    # 4-5. 생성된 문자열 반환
    return answer    