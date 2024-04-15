'''
https://school.programmers.co.kr/learn/courses/30/lessons/42746

[정렬] 가장 큰 수

아래 코드는 시간 초과됨!

def solution(numbers):
    zeros = []
    number = []
    maxNum = ""
    for num in numbers:
        if num == 0:
            zeros.append(str(num))
        else:
            number.append(str(num))
    
    answer = ''
    while (len(number) != 1):
        maxNum = number[0]
        for num in number[1:]:
            if maxNum[0] == num[0]:
                if len(maxNum) == len(num):
                    if maxNum < num:
                        maxNum = num
                else:
                    if (len(maxNum) > len(num)) and maxNum[-1] == "0":
                        maxNum = num
                    else:     
                        if num[-1] != "0":
                            maxNum = num
            elif maxNum[0] < num[0]:
                maxNum = num
        answer += maxNum
        number.remove(maxNum)
    answer += number[0]
    answer += "0"*len(zeros)
    print(answer)

    return answer

solution([0,0,3,330,334, 5, 9])

'''

def solution(numbers):
    zeros = []
    number = []
    answer=''
    for num in numbers:
        if num == 0:
            zeros.append(str(num))
        else:
            number.append(str(num))
    if len(number) == 0:
        return "0"
    number.sort(key=lambda num: num*3, reverse=True)
    answer = ''.join(number) + "0"*len(zeros)
    print(answer)

solution([0,0,3,330,334, 5, 9])