N = int(input())
data = list(map(int,input().split()))

#고정점 찾기
def find_fix_dot(array, start, end):
    if start > end :
        return None
    mid = (start + end) // 2

    #숫자와 인덱스가 같으면 고정점
    if(mid == array[mid]):
        return mid
    #인덱스가 숫자보다 크면 더 큰쪽에서 다시찾기
    elif(mid > array[mid]):
        return find_fix_dot(array, mid+1, end)
    #인덱스가 숫자보다 작으면 작은 쪽에서 다시찾기
    else:
        return find_fix_dot(array, start, mid-1)

result = find_fix_dot(data, 0, N-1)


if result == None:
    print(-1)
else:
    print(result)
    