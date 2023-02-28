from typing import List


# 특정 원소가 속한 집합의 루트 노드 찾기
def find(parent: List[int], x):
    # 자기 자신을 가리킬 때가지.
    if parent[x] != x:
        # 경로 압축 기법으로 루트 노드를 미리 캐싱해두기
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: List[int], a: int, b: int):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
print(parent)

for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)
    print(*parent)

print('각 원소가 속한 집합의 루트')
print(*[i for i in range(1, v + 1)])
for i in range(1, v + 1):
    print(find(parent, i), end=' ')
print()

print('부모 테이블')
print(*[i for i in range(1, v + 1)])
for i in range(1, v + 1):
    print(parent[i], end=' ')
print()
