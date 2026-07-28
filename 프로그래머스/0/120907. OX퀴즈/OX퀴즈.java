/**
기호의 안에 있는 계산이 맞는지 안맞는지 보고 풀어서 O X를 기록하면되는거네 
*/
import java.util.*;
class Solution {
    public ArrayList<String> solution(String[] quiz) {
        ArrayList<String> answer = new ArrayList<String>();
        
        for(String problem : quiz){
            // 먼저 수식을 나누어 정리한다. 아 수식도 같이 정리해야한다.
            String[] num = problem.split(" ");
            // 이제 숫자인경우는 저장 기호인 경우는 계산을 해야한다.
            // 근데 사실 개수가 정해진 이 문제는 숫자만 뽑고 기호만 뽑아서 계산하면 빠르게먹힌다.
            boolean ans = false;
            if(num[1].equals("+")){
                ans = (Integer.parseInt(num[0]) + Integer.parseInt(num[2])) == Integer.parseInt(num[4]);
            }
            else{
                ans = (Integer.parseInt(num[0]) - Integer.parseInt(num[2])) == Integer.parseInt(num[4]);
            }
            
            if(ans){
                answer.add("O");
            }
            else{
                answer.add("X");
            }
        }
        
        return answer;
    }
}