#문자열 뒤집기
str1=input()
cnt=0
com=-1
result=0
for i in range(len(str1)):
    if com != int(str1[i]):
        cnt=cnt+1
        com=int(str1[i])
result=cnt//2
print(result)
