/*
1. digit면 list에 추가
2. 알파벳이면 쌓으면서 검사 Map에
3. 
*/

import java.util.*;

class Solution {
    public int solution(String s) {
        Map<String,Integer> book = new HashMap<String,Integer>(Map.of(
            "zero",0,
            "one",1,
            "two",2,
            "three" ,3,
            "four",4,
            "five",5,
            "six",6,
            "seven",7,
            "eight",8,
            "nine",9
        ));
        String answer = "";
        String str = "";
        for(int i = 0; i < s.length() ; i++){
            if(Character.isDigit(s.charAt(i))) answer += s.charAt(i);
            else{
                str += s.charAt(i);
                if(book.containsKey(str)) {
                    answer += book.get(str);
                    str = "";
                }
            }
        
        }
        return Integer.parseInt(answer);
    }
}