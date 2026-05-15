# =====================================================================
#   1181번:    단어 정렬
#   @date:   2026-02-02
#   @link:   https://www.acmicpc.net/problem/1181
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
아아디어:
    제일먼저 받은 N 만큼 반복해서 입력을 받아들인데 이걸 바로 dict으로 만들어서
    단어 : 길이 -> 이런식으로 정렬을 먼저 해야할꺼같다.
    이렇게하면 같은 단어는 자동으로 사라진다.
    그리고 이제 사전순으로 정렬하걸걸 하면된다.
"""


import sys

input = sys.stdin.readline
out = sys.stdout.write
# 먼저 입력받는다
N = int(input())
# dict 생성
words = {}
for _ in range(N):
    w = input().strip()
    words[w] = len(w)


# 단어 dict를 value값으로 정렬하기
words = sorted(words.items(), key=lambda x: x[1])


List = {j: [] for i, j in words}


for i, j in words:
    # 같은 글자수 인애들 모아야지
    # dict로 그냥 추가해야겟다
    List[j].append(i)
for i, j in List.items():
    List[i] = sorted(j)

# 길이 오름차순으로 출력 + 같은 길이면 사전순
for i in List:
    for j in List[i]:
        out(str(j) + "\n")
