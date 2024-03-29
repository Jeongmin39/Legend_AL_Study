#곱하기 또는 더하기
nums=input()
numlist=[]
result=1
cnt=0
for i in range(len(nums)):
    if int(nums[i])==0:
       pass
    elif int(nums[i])==1:
        cnt=cnt+1
    else:
        numlist.append(nums[i])
for j in range(len(numlist)):
    result=result*int(numlist[j])
result=result+cnt
print(result)