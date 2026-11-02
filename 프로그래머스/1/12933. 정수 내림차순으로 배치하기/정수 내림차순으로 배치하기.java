import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        char[] list = (n + "").toCharArray();
        
        Arrays.sort(list);
        String s = "";
        for(int i = list.length -1 ; i >= 0; i--){
            s += list[i];
        }
        
        answer = Long.parseLong(s);
        
        return answer;
    }
}