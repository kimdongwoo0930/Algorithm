# =====================================================================
#   10816번:    숫자 카드 2
#   @date:   2026-02-05
#   @link:   https://www.acmicpc.net/problem/10816
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline
out = sys.stdout.write

N = int(input())
List = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))
# count를 쓰면 모두 한번씩 확인하기 때문에 시간초과가 뜬다
book = {}
for i in List:
    if i in book:
        book[i] += 1
    else:
        book[i] = 1

for i in chk:
    if i in book:
        out(str(book[i]) + " ")
    else:
        out(str(0) + " ")
