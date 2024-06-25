'''

def findMax_profit(sum_date, result):
    global maxResult
    
    #print("sum date: "+str(sum_date))
    if sum_date+consult[sum_date][0] >= N:
        maxResult = max(result, maxResult)
        #print("max : "+str(maxResult))
    else:
        result += consult[sum_date][1]
        findMax_profit(sum_date+consult[sum_date][0], result)
        
for i in range(N):
    #print("i: "+(str(i)))
    findMax_profit(i, 0)
print(maxResult)

'''
N = int(input())
consult = []
profitTable = [0] * (N + 1)
maxResult = 0

for _ in range(N):
    consult.append(list(map(int, input().split())))
        
for i in range(N-1, -1, -1):
    if consult[i][0] + i > N:
        profitTable[i] = maxResult
    else:
        profitTable[i] = max(consult[i][1]+profitTable[consult[i][0] + i], maxResult) 
        maxResult = profitTable[i]
    
print(maxResult)