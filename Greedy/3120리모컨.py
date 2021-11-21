def button10(a,b):
    if a <= b:
        return a + 10
    else:
        return a - 10

def button5(a,b):
    if a <= b:
        return a + 5
    else:
        return a - 5

def button1(a,b):
    if a <= b:
        return a + 1
    else:
        return a - 1

a,b = map(int,input().split()) # 현재 온도 7, 목표 온도 34
count = 0

while True:
    if a == b:
        break
    
    if abs(b-a) >= 10:
        a = button10(a,b)
        count += 1
        continue
    
    elif abs(b-a) >= 5:
        check10 = button10(a,b)
        check5 = button5(a,b)
    
        if abs(b-check10) < abs(b-check5):
            a = check10
        else:
            a = check5
        
        count += 1
        continue
        
    else:
        check5 = button5(a,b)
        check1 = button1(a,b)
        
        if abs(b-check5) < abs(b-check1):
            count += abs(b-check5) + 1
        else:
            count += abs(b-check1) + 1
        break

print(count) # 5

'''
입력
7
34

결과
5
'''
