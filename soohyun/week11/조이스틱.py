from collections import deque


def solution(name: str) -> int:
    movement = 0

    for alpha in name:
        alpha_move = min(ord(alpha) - ord("A"), 26 - (ord(alpha) - ord("A")))
        movement += alpha_move

    not_a_indices = deque([index for index in range(len(name)) if name[index] != "A"])
    
    # 갔다가 돌아오는 경우.
    forth_and_back = 0
    now = 0
    while not_a_indices:
        forth = not_a_indices[-1] - now
        back = now + len(name) - not_a_indices[0]
        print(forth_and_back, forth, back)
        if forth >= back:
            forth_and_back += back
            break
        else:
            nxt = not_a_indices.popleft()
            forth_and_back += nxt - now 
            now = nxt
    
    print(forth_and_back)
    movement += forth_and_back
    return movement

