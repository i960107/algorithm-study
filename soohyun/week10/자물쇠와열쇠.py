from typing import List


def solution_fail(key:List[List[int]], lock:List[List[int]]) -> bool:
    n = len(lock)
    
    def make_bin(arr:List[List[int]]):
        bin_arr = []
        for row in arr:
        	temp  = 0
        	for index in range(len(row)):
        		temp = temp * 2 + row[index]
        	bin_arr.append(temp)
        return bin_arr
        
        
    row_goal =  1 << (n - 1)
    
    def _solution(bin_key, bin_lock):
        for shift_horizontal in range(-n, n):
            for shift_vertical in range(-n, n):
                found = True
                for r, row_lock in enumerate(bin_lock, 1):
                    if shift_vertical >= 0 and shift_vertical <= r:
                        if shift_horizontal < 0:
                            row_key = bin_key[r - shift_vertical] << abs(shift_horizontal)
                        else:
                            row_key = bin_key[r - shift_vertical] >> abs(shift_horizontal)
                    else:
              	        row_key = 0
                        
                    if(row_key ^ row_lock != row_goal):
                        found = False
                        break
                if found:
                    return True
        return False
                
    bin_lock = make_bin(lock)
    def rotate(arr):
        n = len(arr)
        result = []
        for c in range(n):
            row = []
            for r in range(n-1, -1, -1):
                row.append(arr[r][c])
            result.append(row)
        return result
            
    bin_lock = make_bin(lock)
    bin_key = make_bin(key)
    if _solution(bin_key, bin_lock):
        return True
    
    prev = key
    for _ in range(3):
        rotated = rotate(prev)
        if _solution(bin_key, bin_lock):
            return True
        
    return False

def solution(key:List[List[int]], lock:List[List[int]]) -> bool:
    def rotate(arr:List[int]):
        n = len(arr)
        result = [[0] * n for _ in range(n)]
        
        for r in range(n-1, -1, -1):
            for c in range(n):
                result[c][-r + n - 1] = arr[r][c] 
        return result
    
    K = len(key)
    L = len(lock)
    
    def check(new_lock):
        n = len(new_lock) // 3
        for i in range(n, n*2):
            for j in range(n, n * 2):
                if new_lock[i][j] != 1:
                    return False
        return True
        
    
    new_lock = [[0] * (L * 3) for _ in range(L * 3)]
    for i in range(L):
        for j in range(L):
            new_lock[L+i][L+j] = lock[i][j]
    
    for _ in range(4):
        for i in range(1, L*2):
            for j in range(1, L*2):
                for x in range(K):
                    for y in range(K):
                        new_lock[i+x][j+y] += key[x][y]
                        
                if check(new_lock):
                    return True
                
                for x in range(K):
                    for y in range(K):
                        new_lock[i+x][j+y] -= key[x][y]
        key = rotate(key)
    return False
                

