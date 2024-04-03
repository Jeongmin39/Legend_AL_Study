N = input()

luckystraight = 0
for m, n in enumerate(N):
    if m < len(N) // 2:
        luckystraight += int(n)
    else:
        luckystraight -= int(n)
        
if luckystraight == 0:
    print("LUCKY")
else:
    print("READY")