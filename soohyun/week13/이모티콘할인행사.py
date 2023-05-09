from typing import List
from itertools import combinations_with_replacement, permutations


def solution(users:List[List[int]], emoticons:List[int]) -> List[int]:
    answer = [0, 0]
    # 4 ^ 7가지 경우의수 -> dfs 가능.
    discounts = (10, 20, 30, 40)
    # combinations_with_replacement는 중복 순열은?
    def calculate_cost(discounts:List[int], threshold:int) -> int:
        cost = 0
        for discount, original_price in zip(discounts, emoticons):
            if discount >= threshold:
                cost +=  original_price * (100 - discount) / 100
        return cost
        
             
    for combi in combinations_with_replacement(discounts, len(emoticons)):
	#시간초과 set으로 해결
        for permu in set(permutations(combi)):
        	emoticon_plus = 0
        	sales = 0
            
        	for threshold, max_budget in users:
        		cost = calculate_cost(permu, threshold)
                
       			if cost < max_budget:
          			sales += cost
        		else:
        			emoticon_plus += 1
                
        	if emoticon_plus > answer[0]:
        	    answer = [emoticon_plus, sales]
                
        	elif emoticon_plus == answer[0] and sales > answer[1]:
        	    answer[1] = sales
    return answer
