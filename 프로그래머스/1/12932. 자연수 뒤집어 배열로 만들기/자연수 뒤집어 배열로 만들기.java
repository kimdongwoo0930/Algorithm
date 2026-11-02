import java.util.*;

class Solution {
    public int[] solution(long n) {
        
        char[] s = (n + "").toCharArray();
        
        int[] answer = new int[s.length];
        
        for(int i = s.length; i >= 1; i--){
            answer[s.length - i] = s[i-1] - '0';
        }
        
        
        return answer;
    }
}