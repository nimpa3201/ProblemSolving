import heapq
n = int(input())
pq =[]

for i in range(n):
    arr =map(int,input().split())
    for num in arr:
        heapq.heappush(pq,num)
        if len(pq) > n:
            heapq.heappop(pq)
ans=heapq.heappop(pq)
print(ans)

