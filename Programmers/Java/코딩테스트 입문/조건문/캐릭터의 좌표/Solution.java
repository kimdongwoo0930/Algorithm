
import java.util.*;
class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {};
        
        int x = 0;
        int y = 0;
        
        for(String dir : keyinput){
            switch(dir){
                    case "left" -> x -= 1;
                    case "right" -> x += 1;
                    case "up" -> y += 1;
                    case "down" -> y -= 1;
            }
            if (Math.abs(x) > board[0] / 2) {
                x = x < 0 ? -(board[0] / 2) : board[0] / 2;
            }
            if (Math.abs(y) > board[1] / 2){
                y = y < 0 ? -(board[1] / 2) : board[1] / 2;
            }
        }
        answer = new int[]{x,y};
        
        return answer;
    }

    // 제출할 땐 이 아래는 지우고 solution만 붙여넣기
    public static void main(String[] args) {
        Solution s = new Solution();

        // 기대값 [2, 1]
        System.out.println(Arrays.toString(
                s.solution(new String[] {"left", "right", "up", "right", "right"}, new int[] {11, 11})));

        // 기대값 [0, -4]
        System.out.println(Arrays.toString(
                s.solution(new String[] {"down", "down", "down", "down", "down"}, new int[] {7, 9})));
    }
}
