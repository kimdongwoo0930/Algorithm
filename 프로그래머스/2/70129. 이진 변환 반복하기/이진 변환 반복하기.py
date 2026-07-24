def solution(s):
    answer = []
    zero = 0
    num = s
    fun = 0
    zin = ""
    cnt = 0
    
    
    while 1:
        cnt += 1
        zero += num.count('0')
        for i in range(len(num)):
            if num[i] != '0':
                zin += num[i]
                
        print(num, zero)
                
        fun = len(zin)
        zin = ""
        while 1:
            if fun < 2:
                zin += '1'
                break
            zin += str(fun % 2)
            fun = fun // 2
            
        if zin == '1':
            break        
        
        num = zin[::-1]
        zin = ""
        
    answer = [cnt,zero]

    
    return answer