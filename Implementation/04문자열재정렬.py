s = input()
result = []
value = 0

for i in s:
  if i.isalpha():
    result.append(i)
  else:
    value += int(i)

result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result)) # 공백 없이 일렬로 나열해서 출력

'''
입력 ab8db7
결과 abbd15
'''
