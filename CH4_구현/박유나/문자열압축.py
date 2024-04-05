#Q09

def solution(s):
    answer=[]
    if len(s)==1:
        return 1
    for i in range(1, (len(s)//2)+1):
        str1 = ''
        cnt = 1
        tmp=s[:i]
        for j in range(i, len(s), i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    str1 = str1 + str(cnt)+tmp
                else:
                    str1 = str1 + tmp
                tmp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            str1 = str1 + str(cnt) + tmp
        else:
            str1 = str1 + tmp   
        answer.append(len(str1))
    return min(answer)