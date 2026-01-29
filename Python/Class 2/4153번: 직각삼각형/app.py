#=====================================================================
#   4153번:    직각삼각형                   
#   @date:   2026-01-29              
#   @link:   https://www.acmicpc.net/problem/4153  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

'''
3변의 길이 받아서 오른차순하고
1번 제곱 + 2번 제곱 = 3번 제곱 이면 직각삼각 아니면 Wrong
'''

import sys;

input = sys.stdin.readline
while 1:
    List = list(map(int, input().split()))
    if List[0] == 0:
        break
    List.sort()
    if (List[0] ** 2 + List[1] ** 2)  == List[2] ** 2:
        print("right")
    else:
        print("wrong")
    

