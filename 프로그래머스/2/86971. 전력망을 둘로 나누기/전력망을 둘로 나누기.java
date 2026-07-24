import java.util.*;

/**
계속 앞에서부터 잘라보면서 가장 작은걸 구하면 된다.
1 - 3 사이를 짜르고 1과 연결된걸 구하고
3과 연결된걸 구해서 둘이 뺴고
2 - 3 사이를 자르고 똑같이 구하고
3 - 4 짜르고 또 구하고 이런식으로 하면 되는거 같다.

구현순서
- 처음에 받은 개수로 index를 뽑아서 리스트 2개를 만들어서 
 [ 1 ], [ 3 ] -> [2,3] 이면 [ 1 ], [ 2, 3 ] 이런식으로 추가하고 
 마지막에 끝날때 각 리스트의 개수를 서로 빼고 절대값을 하면 그게 차이 개수아닐까 싶다.
*/
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 9999;
        
        for(int i = 0 ; i < n - 1; i++){
            /* 첫번째부터 짤라야한다 */
            Set<Integer> A = new HashSet<>();
            A.add(wires[i][0]);
            Set<Integer> B = new HashSet<>();
            B.add(wires[i][1]);
            
            /* 이제 연결 개수 확인해야함 */
            boolean changed = true;
            while (changed) {
                changed = false;
                for (int[] target : wires) {
                    if (target == wires[i]) continue; // 배열은 참조 비교로 충분 (같은 객체인지)

                    if (A.contains(target[0]) || A.contains(target[1])) {
                        if (A.add(target[0])) changed = true;
                        if (A.add(target[1])) changed = true;
                    }

                    if (B.contains(target[0]) || B.contains(target[1])) {
                        if (B.add(target[0])) changed = true;
                        if (B.add(target[1])) changed = true;
                    }
                }
            }

            System.out.println(A + " " + B);
            answer = Math.min(answer, Math.abs(A.size() - B.size()));
            }
            
                 return answer;   
        }
    }