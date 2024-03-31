n = int(input())
coin = list(map(int,input().split()))
coin.sort()

target = 1
for num in coin:
  if num > target:
    break
  else:
    target+=num
 
print(target)

# test n=5 , 3 2 1 1 9
#1 sort. 1 1 2 3 9
#2 target 1을 만들 수 있는지 보기
#2-1 , 1 > 1 , 새로 들어오는 수 num 1이 target 1보다 작거나 같아서 target을 만들 수 있음 다음 타겟을 2로함
#2-2 , 2 > 2 , 새로 들어오는 수 num 2이 target 2보다 작거나 같아서 target을 만들 수 있음 다음 타겟을 4로함
# 다음 타겟을 4로 하는 이유는 3은 1+2로 만들 수 있어서
#2-3  