/*
일단 푼다는 가정
매번 자기 문자를 0번부터 자기번째까지 검사를한다.
*/

import java.util.*;

class Solution {
    public List<Integer> solution(String s) {
       List<Integer> answer = new ArrayList<>();
        
        for(int i = 0; i < s.length() ; i++){
            char c = s.charAt(i);
            if(s.indexOf(c) == i) {
                answer.add(-1);
                continue;
            }
            int index = 0;
            for(int j = 0 ; j < i; j++){
                if(s.charAt(j) == c) index = j;
            }
            answer.add(i - index);
        }
        
        
        return answer;
    }
}