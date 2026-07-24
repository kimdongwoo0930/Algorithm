answer = 0
visited = []
N = 0

def dfs(k, cnt, dungeons):
    global answer
    answer = max(cnt,answer)
    
    for j in range(N):
        if not visited[j] and k>= dungeons[j][0]:
            visited[j] = True
            dfs(k-dungeons[j][1], cnt + 1, dungeons)
            visited[j] = False
    
    
    
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [False] * N
    
    dfs(k, 0 ,dungeons)
        
        
    
    
    return answer