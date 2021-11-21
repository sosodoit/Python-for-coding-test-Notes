n = int(input())
plan = input().split()
k = ['L','R','U','D']
x, y = 1, 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for p in plan:
  for i in range(len(k)):
    if p == k[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x,y=nx,ny

print(x,y)

'''
입력
5
R R R U D D

결과
3 4
'''
