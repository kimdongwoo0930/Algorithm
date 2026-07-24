List = {"R" : 0, "T" : 0, "C" : 0 , "F" : 0, "J": 0, "M" : 0, "A" : 0, "N" : 0}

Al = [["R","T"],["C","F"],["J","M"],["A","N"]]


def check(a,b):
    if List[a] > List[b]:
        return a
    elif List[a] == List[b]:
        return a
    else: return b
    

def solution(survey, choices):
    global List
    answer = ""
    
    for i in range(len(survey)):
        l = survey[i][0]
        k = survey[i][1]
        
        
        if choices[i] < 4:
            List[l] += (4 - choices[i]) 
        else:
            List[k] += (choices[i] - 4)
        
    for i in Al:
        answer += check(i[0],i[1])
        
    return answer