# =====================================================================
#   10814번:    나이순 정렬
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/10814
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
나이가 적은 순으로 출력을 하고, 나이가 같다면 먼저 가입한 순으로 출력한다.
1. 난 왜 자꾸 dict만 생각이 날까 싶다

{1 : [] ~ 200: []}
"""

people = {i: [] for i in range(1, 201)}

import sys

input = sys.stdin.readline
out = sys.stdout.write

N = int(input())

for _ in range(N):
    age, name = input().split()
    people[int(age)].append(name)

for i, j in people.items():

    if j == []:
        continue
    else:
        for k in j:
            out(str(i) + " " + str(k) + "\n")
