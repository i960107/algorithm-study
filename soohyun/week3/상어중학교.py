from typing import List


def solution(n: int, m: int, graph: List[List[int]]) -> int:
    pass


def gravity(graph: List[List[int]]) -> int:
    pass


def get_benchmark_of_largest_block(n: int, graph: List[List[int]]) -> int:
    final_i, final_j = 0, 0
    blocks = 0
    rainbow_blocks = 0

    for r in range(n):
        for c in range(n):
            if 1 <= graph[r][c]:
                pass


def get_blocks_by_bfs(n: int, graph: List[List[int]], r: int, c: int) -> int:
    # 매개변수가 2개일때 어떻게 반환하는 게 좋을까...
    blocks = 0
    return 0


n, colors = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
