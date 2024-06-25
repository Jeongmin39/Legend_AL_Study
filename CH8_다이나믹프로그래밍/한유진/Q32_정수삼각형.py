''' 재귀 방식은 틀렸다고 나옴!
n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

maxResult = 0
def find_max_route(step, current_index, result):
    global maxResult
    result += triangle[step][current_index]
    
    if step == 4:
        if result > maxResult:
            maxResult = result
        return
    
    find_max_route(step+1, current_index, result)
    find_max_route(step+1, current_index+1, result)
            
find_max_route(0, 0, 0)
print(maxResult)
'''

# 왜 for문이 재귀보다 효율적일까...?

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):   
        if j == 0: triangle[i][j] += triangle[i-1][j]
        elif j == i: triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))