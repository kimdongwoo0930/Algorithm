import java.util.*;

/*
 번호를 n개씩 끊는게 아니라 n = 3이면 123456 -> 123, 234, 345
*/

class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        long number = Long.parseLong(p);
        
        for(int i = 0; i <= t.length() - p.length(); i++){
            // 길이만큼 뽑아서 비교
            String num = t.substring(i,i + p.length());
            if(Long.parseLong(num) <= number) answer++;
        }
        
        return answer;
    }
}