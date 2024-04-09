def checkRules(answer):
    for x, y, a in answer:
        if a == 0: # column
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a == 1: # beam
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0: # delete
            answer.remove([x, y, a])
            if not checkRules(answer):
                print("cannot remove: ["+str(x)+", "+str(y)+", "+str(a)+"]")
                answer.append([x, y, a])
        elif b == 1: # install
            answer.append([x, y, a])
            if not checkRules(answer):
                print("cannot install: ["+str(x)+", "+str(y)+", "+str(a)+"]")
                answer.remove([x, y, a])
    
    return sorted(answer)

answer = solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
print(answer)