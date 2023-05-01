def solution(numbers, hand):
    answer = ''
    left, right = [1, 4, 7], [3, 6, 9]
    n_left, n_right = 10, 12
    l_distance, r_distance = 0, 0
    for i in numbers:
        if i in left:
            answer += 'L'
            n_left = i

        elif i in right:
            answer += 'R'
            n_right = i

        else:
            if i == 0 :
                i = 11
            
            l_distance = abs(i - n_left)
            r_distance = abs(i - n_right)

            if l_distance // 3 + l_distance % 3 > r_distance // 3 + r_distance % 3:
                n_right = i
                answer += 'R'
            elif l_distance // 3 + l_distance % 3 < r_distance // 3 + r_distance % 3:
                n_left = i
                answer += 'L'
            else:
                if hand == 'right':
                    n_right = i
                    answer += 'R'
                else:
                    n_left = i
                    answer += 'L'      

    return answer