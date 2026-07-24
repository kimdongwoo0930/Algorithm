def solution(char):
    
    st = []
    answer = 0
    
    for i in range(len(char)):
        st.append(char[i])
        if len(st) > 3:
            if st[-4:] == [1,2,3,1]:
                answer += 1
                for i in range(4):
                    st.pop()
    
    return answer