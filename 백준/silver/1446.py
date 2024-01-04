import heapq
import sys
INF = sys.maxsize
n,d= map(int,input().split())
dist= [INF for _ in range(d+1)]
graph = [[] for _ in range(d+1)]
arr =[]
pq =[]
arr.append((0,0,0))
arr.append((d,d,0))
for _ in range(n):
    start,end,length = map(int,input().split())
    if start > d or end > d or end-start < length :
        continue
    arr.append((start,end,length))
arr.sort()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j][0]-arr[i][1]>0:
            arr.append((arr[i][1],arr[j][0],arr[j][0]-arr[i][1]))
for s,e,w in arr:
    graph[s].append((e,w))

def dijkstra(end):
    dist[0] =0
    heapq.heappush(pq,(0,0))
    while pq:
        min_dist, min_index = heapq.heappop(pq)

        if dist[min_index] != min_dist :
            continue

        for target_index,target_dist in graph[min_index]:
            new_dist = min_dist+target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return dist[end]
print(dijkstra(d))
