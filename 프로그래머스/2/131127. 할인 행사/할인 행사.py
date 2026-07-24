def solution(want, number, discount):
    
    Len = len(discount) - 1
    answer = 0
    cnt = 0
    bol = True
    
    for i in range(len(discount)):
        if i+9 > Len:
            d_list = discount[i::]
            for j in range(len(want)):
                if d_list.count(want[j]) != number[j]:
                    bol = False
                    break
            if bol:
                cnt += 1
            bol = True

            break
        else:
            d_list = discount[i:i+10]
            for j in range(len(want)):
                if d_list.count(want[j]) != number[j]:
                    bol = False
                    break
            if bol:
                cnt += 1
            bol = True
    answer = cnt
    return answer