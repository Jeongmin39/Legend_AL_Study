N=input()
l=(len(N)//2)
p=0
n=0
for i in range(l):
    p=p+int(N[i])
for j in range(l):
    n=n+int(N[-1-j])
if p==n:
    print("LUCKY")
else:
    print("READY")