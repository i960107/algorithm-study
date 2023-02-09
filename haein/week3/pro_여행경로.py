from collections import deque
def solution(tickets):
    answer = []
    destinations = {}  # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    visited = []

    for a, b in tickets:
        if a not in destinations.keys() or b not in destinations.keys():
            destinations[a] = [(b, False)]
            destinations[b] = []
        else:
            destinations[a].append((b, False))

    def bfs(v):
        queue = deque([v])
        visited.append('ICN')

        while queue:
            start = queue.popleft() # 'ICN'
            # start : [(a, False)]
            # ATL : [(ICN, True), (SFO, False)]
            # 'ATL': [('ICN', False), ('SFO', False)]}
            for a, b in destinations[start]: # 'SFO', 'ATL'
                if a not in visited:
                    # if not b:
                    #     for k, t in destinations[a]:
                    #         if k == start:
                    #             # destinations[a].remove((k, False))
                    #             destinations[a].append((k, True))
                    # if not b:
                    # destinations[a].remove((a, False))
                    destinations[a].append((a, True))
                    visited.append(a)
                    queue.append(a)
                else:
                    if b == False:
                        visited.append(a)
                        queue.append(a)


    bfs('ICN')
    print(destinations)
    print(visited)

    return answer
