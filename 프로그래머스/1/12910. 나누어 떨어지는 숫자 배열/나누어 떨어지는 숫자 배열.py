def solution(arr, divisor):
    
    answer = []
    arr.sort()
    for i in arr:
        if not i % divisor:
            answer.append(i)
    if not len(answer):
        answer = [-1]
    
    return answer