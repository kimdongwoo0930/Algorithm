# =====================================================================
#   4949번:    균형잡힌 세상
#   @date:   2026-02-04
#   @link:   https://www.acmicpc.net/problem/4949
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""

1. 문자를 쭉 받아들이면서 하나씩 받으면서 숫자를 셀꺼야
어차피 입력은 한번에 받으니까 그냥 다받아서 리스트로 정렬하고 정리하자.

# [ ( ) ]
[ 1. 2. 3. 4 ]
이렇게 정리를 해거꺼다.
[ -> 0번
( -> 1번
) -> 2번
] -> 3번

아 실수 했다 입력이 한번에 들어온다.또 실수했다 (  ) 누가 먼저 열렸는지 확인을 해야한다.


스택으로 해결해보자
[ ( [  다음에 ) 이게 오면 틀린거다.그럼 이미 그 자리에서 no다


"""
import sys

input = sys.stdin.readline

List = []
while True:
    line = input().rstrip()
    if line == ".":
        break
    List.append(line)
for i in range(len(List)):
    List[i] = list(List[i].strip())


for i in List:
    stack = []
    Bool = True
    for j in i:
        if j == "[":
            stack.append(j)
        elif j == "(":
            stack.append(j)
        elif j == "]":
            if len(stack) > 0:
                A = stack.pop()
                if A == "[":
                    continue
                else:
                    Bool = False
                    break
            else:
                Bool = False
                break
        elif j == ")":
            if len(stack) > 0:
                A = stack.pop()
                if A == "(":
                    continue
                else:
                    Bool = False
                    break
            else:
                Bool = False
                break
    if len(stack) > 0:
        Bool = False
    if Bool:
        print("yes")
    else:
        print("no")
