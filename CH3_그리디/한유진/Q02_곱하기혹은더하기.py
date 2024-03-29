S = input()
output = int(S[0])

for i in S[1:]:
    if int(i) <= 1 or output == 0:
        output += int(i)
    else:
        output *= int(i)
        
print(output)