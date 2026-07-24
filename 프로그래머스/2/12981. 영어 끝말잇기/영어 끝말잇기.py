def solution(n, words):
    wl = []
    idx = 1
    answer = []
    member = [0 for i in range(n+1)]
    wl.append(words[0])
    member[idx] += 1
    idx+=1
    check = 0
    check_num = 0
    del words[0]
    for i in words:
        wl_word = wl[-1]
        if((i not in wl) and (wl_word[-1] == i[0])):
            wl.append(i)
            member[idx] += 1
            if(idx == n):
                idx = 1
            else:
                idx += 1
            
        else:
            check = idx
            check_num = member[idx]+1
            break
        
    answer = [check,check_num]

    return answer