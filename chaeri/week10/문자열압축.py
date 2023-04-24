def solution(s):
    ans = len(s) 

    for a in range(1, len(s)//2+1): 
        result = "" 
        slice = s[0:a] 
        cnt = 1 
        for i in range(a, len(s), a):
            if slice == s[i: i+a]:
                cnt += 1 
            else:
                if cnt == 1: 
                    result += slice 
                    slice = s[i: i+a] 
                else: 
                    result += (str(cnt) + slice)
                    cnt = 1 
                    slice = s[i: i+a] 
        
        if cnt == 1: 
            result += slice
        else: result += (str(cnt) + slice)
        ans = min(ans, len(result))
    
    return ans