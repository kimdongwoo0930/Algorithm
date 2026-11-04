import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] list = s.split(" ", -1);
        
        for(int k = 0; k < list.length; k++){
            String st = list[k];
            for(int i = 0; i < st.length(); i++){
                answer += (i % 2 == 0) ? Character.toUpperCase(st.charAt(i)) : Character.toLowerCase(st.charAt(i)); 
            }
            if (k < list.length - 1) answer += " ";
        }        
        return answer;
    }
}