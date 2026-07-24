
def solution(X, Y):
    answer = ''
    nums = []
    
    x = [0 for i in range(10)]
    y = [0 for i in range(10)]
    
    
    for i in X:
        x[int(i)] += 1
    for i in Y:
        y[int(i)] += 1
    # 먼저 같은 숫자를 찾고 (O)
    # 그중에서 만들수 있는 가장큰 숫자를 생각한다.
    
    for i in range(9,-1,-1):
        if i == 0 and answer == '' and x[i] > 0 and y[i] > 0:
            answer = "0"
        elif x[i] > 0 and y[i] > 0:
            answer += str(i) * x[i] if (x[i] < y[i]) else str(i) * y[i]
        

            
    
    if answer == '':
        answer = "-1"
        
    return answer