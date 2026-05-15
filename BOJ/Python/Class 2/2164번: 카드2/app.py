# =====================================================================
#   2164번:    카드2
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/2164
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""
N 을 입력받아 1~ N까지 리스트를 만들고
leftpop을 해서 하나 버리고 나머지 하나더를 leftpop을 해서 맨뒤로 보내자

첫번쨰를 뽑아서 버리고 또 다음껄 뽑아서 맨뒤로 보내기
"""


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
cards = deque(range(1, N + 1))
while 1:
    if len(cards) == 1:
        print(cards.popleft())
        break
    cards.popleft()
    cards.append(cards.popleft())

    
