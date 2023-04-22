from typing import List
from collections import defaultdict
from bisect import bisect_left

def solution(words:List[str], queries:List[str]):
    answer = []
    
    dictionary = defaultdict(list)
    reverse_dictionary = defaultdict(list)
    for word in words:
        dictionary[len(word)].append(word)
        reverse_dictionary[len(word)].append(word[::-1])

    for value in dictionary.values():
        value.sort()
        
    for value in reverse_dictionary.values():
        value.sort()
    
    def find_range(arr:List[str], target):
        if target == "":
            return [0, len(arr)]
        
        left = bisect_left(arr, target)
        if left >= len(arr) or arr[left][:len(target)] != target:
            return [-1, -1]
        # 조건에 해당하는 마지막 글자보다도 항상 뒤에 있음
        after = target + "z" * len(target)
       	right = bisect_left(arr, after)
        return [left, right]
    
    #print(sorted(["fro", "froz", "frs", "frozzzz"]))
    for query in queries:
        wildcard_removed = query.replace("?", "")
        # 접두사
        count = 0
        if query[0] == "?":
            left, right = find_range(reverse_dictionary[len(query)], wildcard_removed[::-1])
        # 접미사
        else:
            left, right = find_range(dictionary[len(query)], wildcard_removed)
                
        answer.append(right - left)
    return answer
