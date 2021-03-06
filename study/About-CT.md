● 가장 출제 빈도가 높은 알고리즘 유형

1. 그리디 (쉬운 난이도)

2. 구현

3. DFS/BFS를 활용한 탐색

<br>

● 복잡도(Complexity) : 알고리즘 성능을 나타내는 척도

1. 시간 복잡도 : 알고리즘 수행 시간

2. 공간 복잡도 : 알고리즘 메모리 사용량

<br>

● 빅오 표기법 (Big-O Notation)

가장 빠르게 증가하는 항만을 고려하는 표기법

즉, 차수가 가장 큰 항만을 고려

<br>

● 알고리즘 설계 TIP

문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)

시간제한이 1초인 문제를 만났을 때,

· N의 범위가 500 : 시간 복잡도가 O(N3)인 알고리즘 설계

· N의 범위가 2,000 : 시간 복잡도가 O(N2)인 알고리즘 설계

· N의 범위가 100,000 : 시간 복잡도가 O(NlogN)인 알고리즘 설계

· N의 범위가 10,000,000 : 시간 복잡도가 O(N )인 알고리즘 설계

<br>

● 알고리즘 문제 해결 과정

1. 지문 읽기 및 컴퓨터적 사고

2. 요구사항(복잡도) 분석

3. 문제 해결을 위한 아이디어 찾기

4. 소스코드 설계 및 코딩

<br>

● 수행 시간 측정 소스코드 예제
``` python
import time
start = time.time()
# ...
end = time.time()
print("수행시간:", end-start)
```

<br>

reference : https://youtu.be/m-9pAwq1o3w
