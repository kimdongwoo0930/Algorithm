#=====================================================================
#   11720번:    숫자의 합                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/11720  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline


N = int(input())
List = list(map(int,input().strip()))

print(sum(List))
