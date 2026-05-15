#=====================================================================
#   15917번:    노솔브 방지문제야!!                   
#   @date:   2026-04-08              
#   @link:   https://www.acmicpc.net/problem/15917  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

powers_of_two = {2 ** n for n in range(31)}

N = int(input())

for i in range(N):
    if int(input()) in powers_of_two:
        print(1)
    else:
        print(0)


