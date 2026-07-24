def prime_num(n):
    if n == 1:
        return False
    for i in range(2,n//2):
        if i > n// i:
            break
        if n % i == 0:
            return False
    return True



def solution(n, k):
    last = ''
    A_list = []
    
    if n == 1:
        answer = 0
    else:
        
        while 1:
            last += str(n % k)
            n = n // k
            if n < k:
                last+= str(n)
                break

        last = (last[::-1])
        nums =(last.split("0"))
        for i in range(len(nums)):
            if nums[i] == '':
                continue
            A_list.append(int(nums[i])) if prime_num(int(nums[i])) else 0



        answer = len(A_list)
    return answer