/*
1. n을 3진법으로 교체
2. 뒤집기
3. 뒤집어서 다시 3진법을 10진법으로 교체
*/


class Solution {
    public int solution(int n) {
        int answer = 0;
        String three = "";
        
        while(n != 0){
            three = n % 3 + three;
            n = (n - (n % 3)) / 3 ;
        }
        
        for(int i= 0; i < three.length(); i++){
            answer +=  (three.charAt(i) - '0') * Math.pow(3,i); 
        }
        
        return answer;
    }
}