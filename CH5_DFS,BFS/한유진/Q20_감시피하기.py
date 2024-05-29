from itertools import combinations

N = int(input())

hallway_info = []
nothing_info = []
teacher_info = []

for i in range(N):
   hallway_info.append(list(input().split())) 
   for j in range(N):
       if hallway_info[i][j] == 'X':
           nothing_info.append((i, j))
       elif hallway_info[i][j] == 'T':
           teacher_info.append((i, j))

def check_Direction(x, y, direction):
    if direction == 0 : # left
        while y>=0 :
            if hallway_info[x][y] == 'S':
                return True
            elif hallway_info[x][y] == 'O':
                return False
            y -= 1
            
    if direction == 1: # right
        while y<N :
            if hallway_info[x][y] == 'S':
                return True
            elif hallway_info[x][y] == 'O':
                return False
            y += 1
            
    if direction == 2: # up
        while x>=0 :
            if hallway_info[x][y] == 'S':
                return True
            elif hallway_info[x][y] == 'O':
                return False
            x -= 1
            
    if direction == 3: # down
        while x<N :
            if hallway_info[x][y] == 'S':
                return True
            elif hallway_info[x][y] == 'O':
                return False
            x += 1
    
    return False

def t_monitor(): # 선생님은 상하좌우로 감시 가능
    for x, y in teacher_info:
        for i in range(4):
            if check_Direction(x, y, i):
                return True
            
    return False

result = "NO"

for object in combinations(nothing_info, 3):
    for x, y in object:
        hallway_info[x][y] = 'O'
        
    if not t_monitor():
        result = "YES"
        break
    
    for x, y in object:
        hallway_info[x][y] = 'X'
    
print(result)