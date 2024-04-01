N=int(input())
nums=sorted(list(map(int,input().split())))
multinums=[]
cntnums=[]
result=N*(N-1)//2
for element in nums:
    cnt=nums.count(element)
    if cnt>1 and element not in multinums:
        multinums.append(element)
        cntnums.append(cnt)
for i in range(len(cntnums)):
    result=result-(int(cntnums[i])*(int(cntnums[i])-1)//2)
print(result)
