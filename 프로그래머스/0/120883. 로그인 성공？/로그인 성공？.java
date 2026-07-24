import java.util.*;

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
        for(String[] list : db){
            if(list[0].equals(id_pw[0])){
                answer = list[1].equals(id_pw[1]) ? "login" : "wrong pw";
            }
        }
        return answer;
    }
}