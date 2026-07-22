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

    // 제출할 땐 이 아래는 지우고 solution만 붙여넣기
    public static void main(String[] args) {
        Solution s = new Solution();

        // 기대값 login
        System.out.println(s.solution(
                new String[] {"meosseugi", "1234"},
                new String[][] {{"rardss", "123"}, {"yyoom", "1234"}, {"meosseugi", "1234"}}));

        // 기대값 wrong pw
        System.out.println(s.solution(
                new String[] {"programmer01", "15789"},
                new String[][] {{"programmer02", "111111"}, {"programmer00", "134"}, {"programmer01", "1145"}}));

        // 기대값 fail
        System.out.println(s.solution(
                new String[] {"rabbit04", "98761"},
                new String[][] {{"jaja11", "98761"}, {"krong0313", "29440"}, {"rabbit00", "111333"}}));
    }
}
