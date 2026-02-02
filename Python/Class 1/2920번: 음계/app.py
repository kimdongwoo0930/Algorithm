#=====================================================================
#   2920번:    음계                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/2920  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

result = ""

List = list(map(int, input().split()))
for i in range(len(List)):
    if i == len(List) - 1:
        print(result)
    elif i == 0:
        if List[i+1] == List[i] + 1:
            result = "ascending"
        elif List[i+1] == List[i] - 1:
            result = "descending"
    else:
        if List[i+1] == List[i] + 1 and result == "ascending":
            result = "ascending"
        elif List[i+1] == List[i] - 1 and result == "descending":
            result = "descending"
        else:
            result = "mixed"