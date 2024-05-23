'''
기존에 구현한 코드는 시간복잡도가 O(N)일 수도 있어서 
수열에서 처음 x가 나오는 부분과 마지막으로 x가 나오는 부분을 찾는 방향으로 
코드를 수정하였다.

def binary_search(lower_bound, upper_bound):
    global count
    
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2
        
        if seq[mid] == x:
            count += 1
                        
            binary_search(lower_bound, mid - 1)
            binary_search(mid + 1, upper_bound)
            break
        elif seq[mid] > x:
            binary_search(lower_bound, mid - 1)
            break
        elif seq[mid] < x:
            binary_search(mid + 1, upper_bound)
            break

            
            
lower_bound = 0
upper_bound = len(seq) - 1
binary_search(lower_bound, upper_bound)
if count != 0:
    print(count)
else:
    print(-1)
'''
N, x = map(int, input().split())
seq = list(map(int, input().split()))
count = 0

def first_binary_search():
    lower_bound, upper_bound = 0, len(seq) - 1
    first_index = -1
    
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2
        
        if seq[mid] == x:
            first_index = mid
            upper_bound = mid - 1
        elif seq[mid] > x:
            upper_bound = mid - 1
        elif seq[mid] < x:
            lower_bound = mid + 1
    return first_index

def last_binary_search():
    lower_bound, upper_bound = 0, len(seq) - 1
    last_index = -1
    
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2
        
        if seq[mid] == x:
            last_index = mid
            lower_bound = mid + 1
        elif seq[mid] > x:
            upper_bound = mid - 1
        elif seq[mid] < x:
            lower_bound = mid + 1
    return last_index

first_val_index = first_binary_search()
last_val_index = last_binary_search()

if first_val_index == -1 and last_val_index == -1:
    print(-1)
else:
    result = last_val_index - first_val_index + 1
    print(result)