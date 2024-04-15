#https://school.programmers.co.kr/learn/courses/30/lessons/42746
#가장 큰 수
def solution(numbers):
    number=list(map(str,numbers))
    #문자열로 바꾸어서 정렬시킴.. 그러나 3은 30보다 앞에 와야함... 어케 할거임?
    #어케하냐면 33 3030으로 만들어서 비교하게 된다면 내가 원하는대로 3이 앞설거임
    #그런데 1000이하의 숫자이므로 331과 3이 온다면 3번은 반복해서 만들어줘야함 그래서 x*3
    number.sort(key=lambda x: x*3,reverse=True)
    answer=''
    for i in range(len(number)):
        answer=answer+number[i]
    #테스트케이스 11만 틀리길래 이건 검색좀 해봄..알고보니 [0,0]의 경우였음 ㅡ..ㅡ 그러면 00이 나와서 틀리게됨 그래서 걍 형변환 조져줌
    answer=int(answer)
    return str(answer)