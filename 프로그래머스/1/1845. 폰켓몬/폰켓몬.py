def solution(nums):
    pocket = []
    num = len(nums) // 2
    
    for i in nums:
        if i not in pocket:
            pocket.append(i)
    
    if len(pocket) < num:
        answer = len(pocket)
    else: 
        answer = num
    
    print(pocket)
    
    return answer