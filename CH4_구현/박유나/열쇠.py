# 주어진 2차원 리스트
matrix = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]

# 행렬을 시계방향으로 90도 회전하는 함수
def rotate_matrix(matrix):
    n = len(matrix)
    # 회전된 행렬을 저장할 빈 리스트 생성
    rotated_matrix = [[None] * n for _ in range(n)]
    # 각 행렬 요소를 회전시켜 새로운 행렬에 저장
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-1-i] = matrix[i][j]
    return rotated_matrix

# 각 행렬 회전별로 출력하기 위한 반복문
for _ in range(4):  # 4번 반복하여 각각 90도씩 회전
    for row in matrix:  # 각 행을 반복하면서 출력
        print(' '.join(row))  # 각 행의 요소를 공백으로 구분하여 출력
    print()  # 한 행이 끝나면 줄바꿈
    matrix = rotate_matrix(matrix)  # 다음 회전을 위해 행렬을 90도 회전시킴
