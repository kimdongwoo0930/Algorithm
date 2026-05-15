#=====================================================================
#   10809번:    알파벳 찾기                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/10809  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

alp = list(map(str,input().strip()))

use = { chr(ord("a") + i ) : -1 for i in range(26) }

for i in range(len(alp)):
    if use[alp[i]] == -1:
        use[alp[i]] = i


print(*list(use.values()))