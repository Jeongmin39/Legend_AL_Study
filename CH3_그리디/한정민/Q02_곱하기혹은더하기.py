num = input()
result = int(num[0])

for i in range(1, len(num)):
    
    data = int(num[i])
    if data <= 1 or result <= 1:
        result += data
    else:
        result *= data

print(result)
