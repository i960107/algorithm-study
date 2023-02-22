def solution(s):
    ans = len(s)
    for unit in range(1, len(s)//2+1):  # 단어를 나누는 단위
        cnt = 1
        comp = ''
        prev = s[:unit]
        for j in range(unit, len(s), unit):
            # 이전단위와 다음단위의 문자가 같다면
            if prev == s[j:j+unit]:
                cnt+=1
            else:   # 다르다면
                comp += str(cnt)+prev if cnt >= 2 else prev
                prev = s[j:j+unit]
                cnt = 1
        comp += str(cnt)+prev if cnt >= 2 else prev
        ans = min(ans, len(comp))
    return ans


