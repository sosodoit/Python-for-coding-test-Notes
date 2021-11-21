pasta = []
ju = []

for _ in range(3):
    pasta.append(int(input()))
for _ in range(2):
    ju.append(int(input()))

dagum = []
for i in pasta:
    for j in ju:
        dagum.append((i+j)+(i+j)*0.1)

print(round(min(dagum),2))
