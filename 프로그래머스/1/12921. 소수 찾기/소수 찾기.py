def solution(n):
    answer = 1
    if n > 2:
        for n in range(3,n+1):
            for i in range(2,n):
                if i * i > n:
                    answer += 1
                    break  
                if not n % i:
                    break
    return answer