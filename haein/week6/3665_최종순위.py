import sys
input = sys.stdin.readline

n = int(input())

'''
사이클이 존재한다면 IMPOSSIBLE 출력
- 진입차수가 0인 노드가 없어 시작노드가 없을 때
- 위상 정렬을 끝냈는 데도 방문하지 않은 정점이 있을 때
'''
