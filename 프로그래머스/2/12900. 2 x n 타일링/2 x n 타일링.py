def solution(n):
    
    st= []
    st.append(1)
    st.append(2)
    st.append(3)
    
    if n > 3:
        for i in range(3,n):
            st.append((st[i-1]+st[i-2])% 1000000007)

    
    answer = st[n-1]
    return answer