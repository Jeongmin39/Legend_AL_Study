def changeDirection(direction, turn):
    if turn == 'L':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction
        
def Dummy():
    N = int(input())
    K = int(input())
    board = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

    # board area
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] = 1

    # apples' location
    for i in range(K):
        m, n = map(int, input().split())
        board[m][n] = 2
        
    L = int(input())
    directionInfo = []
    # direction change info
    for i in range(L):
        x, direc = map(str, input().split())
        directionInfo.append((int(x),direc))
    
    # initial snake direction == east and location (1,1)  
    direction = 0 
    sx, sy = 1, 1
    snakePoint = [(sx, sy)]
    board[1][1] = 3
    time = 0
    
    # [east, north, west, south]
    move_x = [0, -1, 0, 1]
    move_y = [1, 0, -1, 0]
    
    while True:
        nx = sx + move_x[direction]
        ny = sy + move_y[direction]
        
        if board[nx][ny] != 3 and board[nx][ny] != 0:
            if board[nx][ny] == 2:
                board[nx][ny] = 3
                snakePoint.append((nx, ny))
            if board[nx][ny] == 1:
                board[nx][ny] = 3
                snakePoint.append((nx, ny))
                tempx, tempy = snakePoint.pop(0)
                board[tempx][tempy] = 1
        else:
            time += 1
            break
        
        time += 1
        sx, sy = nx, ny
        
        if len(directionInfo) != 0 and time == directionInfo[0][0]:
            direction = changeDirection(direction, directionInfo[0][1])
            directionInfo.pop(0)
    print(time)
    
    
    
Dummy()