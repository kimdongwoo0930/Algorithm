def solution(brown, yellow):
    
    AList = []
    
      
    for i in range(1, yellow + 1):
        if(yellow % i == 0):
            j = yellow// i
            if((i*2) + (j*2) + 4 == brown):
                AList.append([i+2,j+2])
                

    AList.sort(reverse = True)
    answer = AList[0]
    return answer
