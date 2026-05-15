#=====================================================================
#   31403번:    $A + B - C$                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/31403  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

List = [int(input()) for _ in range(3)]
print(List[0] + List[1] - List[2])
print(int(str(List[0]) + str(List[1])) - List[2])
