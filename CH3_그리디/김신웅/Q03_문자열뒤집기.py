number = input()
num0 = 0
num1 = 0
#개수비교하기
for letter in number:
    if letter == '0':
        num0 += 1
    elif letter == '1':
        num1 += 1
        
#작은거 기준으로 그룹 개수 찾기(그룹 개수가 곧 뒤집기 횟수)
min_val = '0' if num0 <= num1 else '1'
groups = 0
current_group = 0

for digit in number:
    if digit == min_val:
          current_group += 1
    else:
        if current_group > 0:
            groups += 1
            current_group = 0
   
if current_group > 0:
    groups += 1

print(groups)
