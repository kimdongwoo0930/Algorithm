def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = b
    ans = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    
    for i in range(a-1):
        day += days[i]
    answer = ans[day%7 - 1]
        
    
    return answer