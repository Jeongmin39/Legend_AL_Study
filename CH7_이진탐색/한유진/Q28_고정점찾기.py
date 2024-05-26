N = int(input())
seq = list(map(int, input().split()))

def find_fixedPoint(lower_bound, upper_bound):
    mid = (lower_bound + upper_bound) // 2
    if lower_bound > upper_bound:
        return -1
    
    if seq[mid] == mid:
        return mid
    elif seq[mid] > mid:
        return find_fixedPoint(lower_bound, mid - 1)
    else:
        return find_fixedPoint(mid + 1, upper_bound)

print(find_fixedPoint(0, N - 1))