#=====================================================================
#   3041번:    N-퍼즐                   
#   @date:   2026-04-07              
#   @link:   https://www.acmicpc.net/problem/3041  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

'''
{ A : (0,0), B: (0,1), C: (0,2) , D: (0,3) , 
E : (1,0), F : (1,1) }

한줄로 dict만들어두고 dict 2개로 만들어서 
비교해서 
'''

# 목표 상태 dict 미리 세팅
goal = {}
for i, c in enumerate('ABCDEFGHIJKLMNO'):
    goal[c] = (i // 4, i % 4)

# 입력 dict
current = {}
for r in range(4):
    line = input().strip()
    for c, ch in enumerate(line):
        if ch != '.':
            current[ch] = (r, c)

# 다른 것만 찾아서 거리 계산
total = 0
for tile in current:
    cr, cc = current[tile]
    gr, gc = goal[tile]
    # 절댓값 계산
    total += abs(cr - gr) + abs(cc - gc)

print(total)