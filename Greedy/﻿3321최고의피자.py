######################################################### 1 
n = int(input()) # 토핑 종류 수
a, b = map(int, input().split()) # 도우, 토핑 가격
c = int(input()) # 도우 칼로리
d = list(map(int, input().split())) # 토핑 칼로리

from itertools import combinations
d2 = list(combinations(d,2))

# 토핑 0개
cash = a
pizza_kcal = c
result = pizza_kcal // cash

# 토핑 1개
if d[0]:
  cash = a + b[0]
  pizza_kcal = c + d[0]
  if result < pizza_kcal:
    result = pizza_kcal // cash
elif d[1]:
  cash = a + b[1]
  pizza_kcal = c + d[1]
  if result < pizza_kcal:
    result = pizza_kcal // cash
  
elif d[2]:
  cash = a + b[2]
  pizza_kcal = c + d[2]
  if result < pizza_kcal:
    result = pizza_kcal // cash

# 토핑 2개
if d2[0]:
  cash = a + b*2
  pizza_kcal = c + d2[0][0] + d2[0][1]
  if result < pizza_kcal:
    result = pizza_kcal // cash
elif d2[1]:
  cash = a + b*2
  pizza_kcal = c + d2[1][0] + d2[1][1]
  if result < pizza_kcal:
    result = pizza_kcal // cash
elif d2[2]:
  cash = a + b*2
  pizza_kcal = c + d2[2][0] + d2[2][1]
  if result < pizza_kcal:
    result = pizza_kcal // cash

print(result)

# ----
# 단순하게 시도, 당연하게 이상쓰한 코드, 값 다르게 나옴
# ----

######################################################### 2
n = int(input()) # 토핑 종류 수
a, b = map(int, input().split()) # 도우, 토핑 가격
c = int(input()) # 도우 칼로리
d = []
for i in range(n):
  d.append(int(input())) # 토핑 칼로리

from itertools import combinations
d2 = list(combinations(d,2))

result = []
t = 2
for i in range(n):
  if i == 0: # 토핑 0개
    cash = a
    pizza_kcal = c
    result.append(pizza_kcal // cash)
  
  elif i == 1: # 토핑 1개
    cash = a + b
    for j in range(len(d)):
      pizza_kcal = c + d[j]
      result.append(pizza_kcal // cash)

  elif i == t: # 토핑 2개
    cash = a + b*i
    for j in range(len(d2)):
      pizza_kcal = c + d2[j][0] + d2[j][1]
    result.append(pizza_kcal // cash)
  t += 1

print(max(result))

'''
입력
8
11 10
572
1110
2530
472
1060
1861
1649
463
430

결과
147

정답
161
'''

# ----
# 잘못된 부분 고쳐가며 수정한 코드
# 그리디를 생각해라.. 최대인 것부터 확인해봐야 하잖아..ㅜ
# ----

######################################################### 3 성공
n = int(input()) # 토핑 종류 수
a, b = map(int, input().split()) # 도우, 토핑 가격
c = int(input()) # 도우 칼로리
d = []
for i in range(n):
  d.append(int(input())) # 토핑 칼로리

d.sort(reverse=True)

result = 0
cash = 0
kcal = 0

for i in d:
  cash += b
  kcal += i
  pizza_kcal = (c+kcal)/float(a+cash)

  if result > pizza_kcal:
    break
  else:
    result = pizza_kcal

print(int(result))
