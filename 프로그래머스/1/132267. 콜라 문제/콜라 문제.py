def solution(a, b, n):
    answer = 0
    last = 0
    
    

    while True:
        if n < a:
            break
        last = n % a
        bottle = (n // a) * b
        answer += bottle
        n = bottle + last
    
    return answer