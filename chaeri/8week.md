# 8week



### 1. 신고 결과 받기

```python
def solution(id_list, report, k):
    answer = []
    result = {}
    fbd_user = []

    for id in id_list:
        result[id] = [[], 0, 0]
    
    for case in set(report):
        result[case.split()[0]][0].append(case.split()[1])
        result[case.split()[1]][1] += 1    

    for user in id_list:
        if result[user][1] >= k:
            fbd_user.append(user)

    for user in id_list:
        for forbidden in fbd_user:
            if forbidden in result[user][0]:
                result[user][2] += 1
        answer.append(result[user][2])

    return answer
```



### 2. 숫자 문자열과 영단어

``` python
def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(arr)):
        s = s.replace(arr[i], str(i))
    return int(s)
```



### 3. 표편집

``` python
def solution(n, k, cmds):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    table = ['O'] * n
    delete = []

    for cmd in cmds:
        cmd = cmd.split()

        if cmd[0] == 'D':
            for _ in range(int(cmd[1])):
                k = linked_list[k][1]

        elif cmd[0] == 'U':
            for _ in range(int(cmd[1])):
                k = linked_list[k][0]

        elif cmd[0] == 'C':
            prev, nxt = linked_list[k]
            table[k] = 'X'
            delete.append((prev, k, nxt))

            if nxt == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == -1:
                linked_list[nxt][0] = prev
            elif nxt == n:
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
        else:
            prev, now, nxt = delete.pop()
            table[now] = 'O'

            if prev == -1:
                linked_list[nxt][0] = now
            elif nxt == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[nxt][0] = now

    return ''.join([x for x in table])
```



### 4. 거리두기 확인하기

``` python
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])
        visited = [[0]*5 for i in range(5)]   
        distance = [[0]*5 for i in range(5)]  
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer
```



### 5. K진수에서 소수개수 구하기

``` python
def k_num(n,k):
    if k == 10:
        return n
    else:
        new_n = ""
        while n > 0:
            new_n += str(n % k)
            n = n // k
        return new_n[::-1]

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    num = k_num(n,k)
    nums = str(num).split("0")
    for x in nums:
        if x and isPrime(int(x)):
            answer += 1
    return answer
```





### 6. 주차 요금 계산

``` python
import math

def solution(fees, records):
    parking = dict()
    stack = dict()
    last_time = 23 * 60 + 59
    answer=[]
    
    for record in records:
        time, car, check = record.split() #시간, 차 번호, IN/OUT
        time_list = list(map(int, time.split(':')))
        minutes = time_list[0]*60 + time_list[1] #분으로 바꿔줌
        
        if parking.get(car):
            if check == 'IN':
                parking[car].append(minutes) #in이면 입차
            elif check == 'OUT': #출차
                if stack.get(car):
                    stack[car] += minutes-(parking[car].pop())
                else:
                    stack[car] = minutes-(parking[car].pop())
        else:
            parking[car] = [minutes]
    
    #출차 안했을 때        
    for key,value in parking.items():
        if value:
            if stack.get(key): # 기록이 남아있다면 23:59분에 출차한 것으로 간주
                stack[key] += (last_time - value[0])
            else:
                stack[key] = (last_time - value[0])
    
    #계산 (문제 제공) 
    for key,value in sorted(stack.items()):
        if value > fees[0]:
            answer.append(fees[1] + math.ceil((value-fees[0])/fees[2])*fees[3]) #올림
        else:
            answer.append(fees[1])
    
    return answer
```

