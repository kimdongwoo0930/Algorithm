def solution(s):
    L = len(s) // 2
    
    if len(s) % 2:
        return s[L]
    return s[L-1:L+1]
    