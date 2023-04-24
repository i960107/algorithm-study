def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(arr)):
        s = s.replace(arr[i], str(i))
    return int(s)