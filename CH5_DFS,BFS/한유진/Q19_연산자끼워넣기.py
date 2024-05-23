N = int(input())

seq = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minVal = 1e9 
maxVal = -1e9

def solve(value, index):
    global add, sub, mul, div, minVal, maxVal
    if index == N:
        minVal = min(value, minVal)
        maxVal = max(value, maxVal)
    else:
        if add > 0:
            add-=1
            solve(value+seq[index], index+1)
            add+=1
        if sub > 0:
            sub-=1
            solve(value+seq[index], index+1)
            sub-=1
        if mul > 0:
            mul-=1
            solve(value+seq[index], index+1)
            mul+=1
        if div > 0:
            div-=1
            solve(value+seq[index], index+1)
            div+=1
        
solve(seq[0], 1)
print(maxVal)
print(minVal)