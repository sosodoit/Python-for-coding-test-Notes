n , k = map(int, input().split())

count = 0

while True:
  
  if n % k == 0:
    n = n // k
  else:
    n -= 1
  count += 1

  if n < k:
    break
 
while n != 1:
  count += (n-1)
  n -= 1

print(n, count)

'''
입력 25 3
결과 1 6
'''
