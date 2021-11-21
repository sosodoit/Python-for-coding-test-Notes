n = int(input())
coin = [50000,10000,5000,1000,500,100,50,10]
count = 0

for i in coin:
    res = n // i
    count += res
    n = n - i*res

print(count)
