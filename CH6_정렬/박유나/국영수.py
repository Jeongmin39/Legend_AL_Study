#q23 국영수

#입력받기
N=int(input())
mylist=[]
for _ in range(N):
    name,kor,eng,math=input().split()
    kor=int(kor)
    eng=int(eng)
    math=int(math)
    mylist.append([kor,eng,math,name])

#정렬하기
mylist.sort(key=lambda x:[-x[0],x[1],-x[2],x[3]])
for i in range(N):
    print(mylist[i][3])