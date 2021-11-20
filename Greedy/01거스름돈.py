n = 1260
count = 0

array = [500,100,50,10]

for coin in array:
  count += n // coin
  n %= coin

print(count)

'''
6
'''

'''
● 시간 복잡도 분석
- 화폐의 종류가 K 라고 할 때, 시간 복잡도는 O(K)
- 화폐의 종류만큼 반복되고 있음
'''
