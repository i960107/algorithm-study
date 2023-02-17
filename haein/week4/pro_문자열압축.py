def solution(s):
    answer = 0
    result = 1002

    def test(s, cur_len):
        test_res = 0
        stack = [[1, s[0:cur_len]]]
        if len(s) % cur_len !=  0:
            test_res += len(s) % cur_len # len(s)가 아니라 s로 해서 실수 했었음
        for i in range(1, len(s) // cur_len):
            cnt, word = stack.pop()
            if word == s[i*cur_len:i*cur_len + cur_len]:
                stack.append([cnt+1, word])
            else:
                stack.append([cnt, word])
                stack.append([1, s[i*cur_len:i*cur_len + cur_len]])
        for a, b in stack:
            if a == 1:
                test_res += cur_len
            else:
                test_res += len(str(a)) + cur_len # a를 str로 바꾸지 않고 해서 실수 했었음
        return test_res

    if len(s) == 1:
        answer = 1
    else:
        for i in range(1, len(s)):
            test_result = test(s, i)
            if result > test_result:
                result = test_result
        answer = result # answer에 result값 넣는 걸 else문 바깥에 둬서 실수 했었음 -> 되도록이면 하나의 변수에 리턴값 모두 통일시키기!

    return answer
