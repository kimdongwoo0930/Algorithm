/**
1. section 첫번째 index부터 롤러를 돌려서 m 을 더한만큼 숫자를 다 빼고 그 후 남은걸 section에서 또 다시 돌린다.
**/

class Solution {
    public int solution(int n, int m, int[] section) {
        if(n <= m){ return 1; }
        int answer = 0;
        int paint = 0;
        for(int num : section){
            if(num > paint){
                answer += 1;
                paint = num + m -1;
            }
        }
        return answer;
    }
}