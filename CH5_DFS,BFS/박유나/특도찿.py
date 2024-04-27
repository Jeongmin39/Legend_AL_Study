from collections import deque

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
print(graph)

for _ in range(m):
    a, b=map(int,input().split())
    graph[a].append(b)
distance=[-1]*(n+1)
distance[x]=0
que=deque([x])
while que:
    now=que.popleft()
    for next_node in graph[now]:
        if(distance[next_node]==-1):
            distance[next_node]=distance[now]+1
            que.append(next_node)
c=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        c=True
if c==False:
    print(-1)
    
