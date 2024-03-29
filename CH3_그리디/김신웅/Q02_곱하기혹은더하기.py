number = input()
result = int(number[0])
for i, num in enumerate(number):
    if i==0:
        continue
    if num==0 or num==1 or result==0 or result==1:
        result += int(num)
    else:
        result *= int(num)

print(result)


