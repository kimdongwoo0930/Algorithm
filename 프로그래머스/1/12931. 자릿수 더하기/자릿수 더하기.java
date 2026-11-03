import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        
        String nums = n + "";
        for(int i=0;i< nums.length();i++
){
            answer += nums.charAt(i) - '0';
            
}

        return answer;
    }
}