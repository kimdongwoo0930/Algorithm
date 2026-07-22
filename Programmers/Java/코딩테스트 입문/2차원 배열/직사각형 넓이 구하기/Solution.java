import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        ArrayList<Integer> X = new ArrayList<>();
        ArrayList<Integer> Y = new ArrayList<>();
        
        for(int[] list : dots){
            if(!X.contains(list[0])) X.add(list[0]);
            if(!Y.contains(list[1])) Y.add(list[1]);
        }
        int answer = Math.abs(X.get(0) - X.get(1)) * Math.abs(Y.get(0) - Y.get(1));
        
    
        return answer;
    }

    // 제출할 땐 이 아래는 지우고 solution만 붙여넣기
    public static void main(String[] args) {
        Solution s = new Solution();

        // 기대값 1
        System.out.println(s.solution(new int[][] {{1, 1}, {2, 1}, {2, 2}, {1, 2}}));

        // 기대값 4
        System.out.println(s.solution(new int[][] {{-1, -1}, {1, 1}, {1, -1}, {-1, 1}}));
    }
}
