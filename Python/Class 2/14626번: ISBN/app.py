# =====================================================================
#   14626번:    ISBN
#   @date:   2026-02-02
#   @link:   https://www.acmicpc.net/problem/14626
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""

index 1 3 1 3 1 3 1 3 1 -> 마지막이면 + N

중간에 다 더하다가  1일때는 나 3일떄 1의 자리수 보고 정해야할듯

아 만약 마지막숫자가 *일경우는 안햇네

"""


import sys

input = sys.stdin.readline
out = sys.stdout.write

num_List = list(input().strip())


index = num_List.index("*")

result = 0

for i in range(len(num_List)):
    if num_List[i] == "*":
        continue
    A = int(num_List[i])
    B = 1 if ((i) % 2 == 0) else 3
    result += A * B


if index + 1 == len(num_List):
    ans = (10 - (result % 10)) % 10
else:
    if (index + 1) % 2 == 1:
        ans = (10 - (result % 10)) % 10
    else:
        for i in range(0, 10):
            if (i * 3) % 10 == (10 - (result % 10)) % 10:
                ans = i
                break

out(str(ans))
