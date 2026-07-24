def solution(n):
    
    st= []
    st.append(0)
    st.append(3)
    st.append(0)
    st.append(11)
    
    if n > 4:
        for i in range(4,n):
            if (i+1) % 2 == 0:
                st.append(st[i-2] * 3 + 2)
                for j in range(i-4,-1,-2):
                    st[i] += st[j] * 2
                st[i] %= 1000000007
                
            else: 
                st.append(0)
    print(st)
    answer = st[n-1]
    return answer