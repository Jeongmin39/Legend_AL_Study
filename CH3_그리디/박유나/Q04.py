#만들 수 없는 금액
N=input()
coins=sorted(list(map(int,list(input()))))
summ=1
for i in range(len(coins)):
    if summ<coins[i]:
        print(summ)
        break
    summ=summ+coins[i]
    