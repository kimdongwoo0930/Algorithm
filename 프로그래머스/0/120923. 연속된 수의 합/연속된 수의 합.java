/**
숫자의 개수와 숫자의 합을 주어지면 연속된 수의 목록을 구하면 된다이거네
문제는 음수부터 올수도 있네 
아 처음에 먼저 123 234 이렇데하다가 목표보다 크면 -1을 하고 시작하는거지 어때 

*/
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int num, int total) {
        // 먼저 첫번째 수를 선언
        int first = 0;
        // 결과가 나올때까지 반복
        while(true){
            int sum = 0;
            ArrayList<Integer> list = new ArrayList<>();
            for(int i = 0; i < num; i++){
                // 순서대로 다 더하기
                int number = first + i;
                list.add(number);
                sum += number;
            }
            if(sum == total){
                return list;
            }
            else if(sum > total){
                first--;
            }
            else if (sum < total){
                first++;
            }
        }
        
    }
}