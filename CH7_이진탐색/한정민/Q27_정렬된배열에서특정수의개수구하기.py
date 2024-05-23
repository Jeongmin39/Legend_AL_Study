N, x = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(array, target):
    start, end = 0, len(array) - 1
    first, last = -1, -1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            if first == -1 or mid < first:
                first = mid
            if mid > last:
                last = mid
            left, right = mid - 1, mid + 1
            # 첫번째, 마지막 위치(인덱스) 찾기
            while left >= start and array[left] == target:
                first = left
                left -= 1
            while right <= end and array[right] == target:
                last = right
                right += 1
            break
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return first, last

first, last = binary_search(data, x)

# first가 -1이면 x가 배열에 없다는 것이므로 -1 출력
if first == -1:
    print(-1)
else:
    print(last - first + 1)