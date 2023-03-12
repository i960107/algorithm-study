from sys import stdin
from collections import defaultdict

N, M, K = map(int, input().split())
adj = defaultdict(list)
# 10,000 C 20다  고려할 수 없음!
for _ in range(M):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))
    adj[b].append((a, t))
