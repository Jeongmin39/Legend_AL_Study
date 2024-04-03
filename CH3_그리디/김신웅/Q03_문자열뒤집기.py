number = input()

#그룹수를 각각 세기위해..
groups_0 = 0
current_group_0 = 0
groups_1 = 0
current_group_1 = 0

for digit in number:
    if digit == '0':
        current_group_0 += 1
        if current_group_1 > 0:
            groups_1 +=1
            current_group_1 = 0
    elif digit == '1':
        current_group_1 += 1
        if current_group_0 > 0:
            groups_0 += 1
            current_group_0 = 0
   
if current_group_0 > 0:
    groups_0 += 1

if current_group_1 > 0:
    groups_1 += 1

print(min(groups_0, groups_1))
