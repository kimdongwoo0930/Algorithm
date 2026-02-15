# =====================================================================
#   1620번:    나는야 포켓몬 마스터 이다솜
#   @date:   2026-02-15
#   @link:   https://www.acmicpc.net/problem/1620
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline

M, N = map(int, input().split())
"""
딕셔너리로 그냥 숫자와 알파벳으로 저장하자
그럼 숫자로도 찾고 알파벳으로도 찾을수 있다.
"""
names = [input().strip() for _ in range(M)]
num_to_name = {i + 1: names[i] for i in range(M)}
name_to_num = {names[i]: i + 1 for i in range(M)}


for _ in range(N):
    Input = input().strip()
    if Input.isdigit():
        print(num_to_name[int(Input)])
    else:
        print(name_to_num[Input])

"""
숫자를 입력한다면 그 위치의 것을 알려주고 글자를 준다면 그 글자가 어디있는지 알려준다

"""
