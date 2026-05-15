#=====================================================================
#   8958번:    OX퀴즈                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/8958  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline


N = int(input())
List = [list(map(str,input().strip())) for _ in range(N)]

for i in List:
    cnt = 1 
    Sum = 0
    for j in i:
        if j == "O":
            Sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(Sum)

        
