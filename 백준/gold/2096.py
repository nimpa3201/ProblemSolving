# 성공 코드 
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_dp = arr[0].copy()
min_dp = arr[0].copy()

for i in range(1, n):
    new_max_dp = [0, 0, 0]
    new_min_dp = [9 * n + 1, 9 * n + 1, 9 * n + 1]

    new_max_dp[0] = max(max_dp[0], max_dp[1]) + arr[i][0]
    new_max_dp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + arr[i][1]
    new_max_dp[2] = max(max_dp[1], max_dp[2]) + arr[i][2]

    new_min_dp[0] = min(min_dp[0], min_dp[1]) + arr[i][0]
    new_min_dp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + arr[i][1]
    new_min_dp[2] = min(min_dp[1], min_dp[2]) + arr[i][2]

    max_dp, min_dp = new_max_dp, new_min_dp

maxAns = max(max_dp)
minAns = min(min_dp)

print(maxAns, minAns)


#메모리 초과 코드 1
# n =int(input())
# arr = [ list(map(int,input().split())) for _ in range(n)]
# max_dp = [[0 for _ in range(3)] for _ in range(n)]
# min_dp = [[0 for _ in range(3)] for _ in range(n)]

# for i in range(3):
#     max_dp[0][i] =arr[0][i]
#     min_dp[0][i] = arr[0][i]
# for i in range(1,n):
#         max_dp[i][0] = max(max_dp[i-1][0],max_dp[i-1][1])+arr[i][0]
#         min_dp[i][0] = min(min_dp[i-1][0],min_dp[i-1][1])+arr[i][0]
#         max_dp[i][2] = max(max_dp[i-1][2],max_dp[i-1][1])+arr[i][2]
#         min_dp[i][2] = min(min_dp[i-1][2],min_dp[i-1][1])+arr[i][2]
#         max_dp[i][1] = max(max_dp[i-1][0],max_dp[i-1][2],max_dp[i-1][1])+arr[i][1]
#         min_dp[i][1] = min(min_dp[i-1][0],min_dp[i-1][2],min_dp[i-1][1])+arr[i][1]
# print(max(max_dp[n-1]),min(min_dp[n-1]))


# 메모리 초과 코드 2
# n =int(input())
# arr = [ list(map(int,input().split())) for _ in range(n)]
# dp = [[[0,0] for _ in range(3)] for _ in range(n)]
# maxAns=0
# minAns=9*n+1
# for i in range(3):
#     dp[0][i][0] =arr[0][i]
#     dp[0][i][1] =arr[0][i]

# for i in range(1,n):
#     for j in range(3):
#         if j ==0:
#             dp[i][j][0] +=max(dp[i-1][j][0],dp[i-1][j+1][0]) +arr[i][j]
#             dp[i][j][1] +=min(dp[i-1][j][1],dp[i-1][j+1][1]) +arr[i][j]
#         if j ==1:
#              dp[i][j][0] +=max(dp[i-1][j-1][0],dp[i-1][j][0],dp[i-1][j+1][0]) +arr[i][j]
#              dp[i][j][1] +=min(dp[i-1][j-1][1],dp[i-1][j][1],dp[i-1][j+1][1]) +arr[i][j]
        
#         if j ==2:
#              dp[i][j][0] +=max(dp[i-1][j][0],dp[i-1][j-1][0]) +arr[i][j]
#              dp[i][j][1] +=min(dp[i-1][j][1],dp[i-1][j-1][1]) +arr[i][j]

# for i in range(3):
#     maxAns = max(maxAns,dp[n-1][i][0])
#     minAns =min(minAns,dp[n-1][i][1])
# print(maxAns,minAns)