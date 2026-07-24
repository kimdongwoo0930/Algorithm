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
}