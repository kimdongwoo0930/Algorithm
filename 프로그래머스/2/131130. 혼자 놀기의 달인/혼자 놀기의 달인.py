def solution(cards):
    answer = 0
    
    for i in cards:
        
        visited = [False] * len(cards)
        cnt_1, idx = 0 , i
        
        while 1:
            if not visited[idx-1]:
                visited[idx-1] = True
                cnt_1 += 1
                idx = cards[idx-1]
            else:
                break
                
        arr = []
        G = 0
        for j in range(len(cards)):
            if not visited[j]:
                arr.append(cards[j])
    
        for k in arr:
            cnt_2 , idx = 0, k
            while 1:
                if not visited[idx-1]:
                    cnt_2 += 1
                    visited[idx-1] = True
                    idx = cards[idx-1]
                else:
                    G = max(G, cnt_2)
                    break
        answer = max(answer, G * cnt_1)
    
    return answer