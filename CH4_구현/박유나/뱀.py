#뱀

#입력받기
N=int(input())
board = [[0]*N for _ in range(N)]
K=int(input())
for _ in range(K):
    a,b= map(int, input().split())
    board[a-1][b-1] = 1  
L=int(input())
move_location=[]
for _ in range(L):
    move_temp_location=[]
    a,b= input().split()
    move_temp_location.append(int(a))
    move_temp_location.append(b)
    move_location.append(move_temp_location)

#뱀 위치 설정
snake=[[0],[0]]

#방향 설정 동->남->서->북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def game():
    # 시작 위치
    i, j = 0, 0
    # 뱀의 시작 위치 저장 (뱀은 2, 사과는 1)
    board[i][j] = 2
    # 현재 방향
    dir = 0
    # 초과 시간
    time = 0
    # 뱀의 몸 위치를 저장
    snake = [(0,0)]

    while True:

        # 다음 위치
        new_x = i + dx[dir]
        new_y = j + dy[dir]

        # 다음 위치에 뱀이 벽에 부딪히거나, 뱀의 몸에 부딪히는지 확인
        if (0 > new_x or new_x >= N or 0 > new_y or new_y >= N or board[new_x][new_y] == 2 ):
            time = time+ 1
            break

        # 다음 위치로 이동할 수 있다면
        else:
            # 다음 위치가 사과라면
            if (board[new_x][new_y] == 1):
                # 뱀 머리 위치 표시
                board[new_x][new_y] = 2
                # 뱀 머리 위치 저장
                snake.append((new_x, new_y))

            # 다음 위치가 사과가 아니라면
            else:
                # 뱀 머리 위치 표시
                snake.append((new_x, new_y))
                # 뱀 머리 위치 저장
                board[new_x][new_y] = 2
                # 뱀 꼬리 위치 저장 제거
                px, py = snake.pop(0)
                # 뱀 꼬리 위치 표시 제거
                board[px][py] = 0

        # 현재 위치 변경
        i, j = new_x, new_y
        # 시간 증가
        time =time+1

        # 방향 전환이 남아있으며, 다음 차례가 방향 전환 시간이라면
        if (len(move_location) >= 1 and time == move_location[0][0]):
            # 오른쪽 방향 전환이라면
            if (move_location[0][1] == 'D'):
                dir = (dir + 1) % 4
            # 왼쪽 방향 전환이라면
            else:
                dir = (dir - 1) % 4

            #  방향 전환했으므로 리스트에서 제거
            move_location.pop(0)

    return time

print(game())

