def solution(s):
    cnt = 0
    char = list(s)
    answer = 0
    
    for _ in range(len(s)):
        
        st = []
        for i in range(len(char)):
            if len(st) > 0 :
                if st[-1] == "[" and char[i] == ']':
                    st.pop()
                elif st[-1] == "(" and char[i] == ')':
                    st.pop()
                elif st[-1] == "{" and char[i] == '}':
                    st.pop()
                else:
                    st.append(char[i])
                
            else:
                st.append(char[i])
        if len(st) == 0:
            answer += 1
                    
        char.append(char.pop(0))
        
    return answer