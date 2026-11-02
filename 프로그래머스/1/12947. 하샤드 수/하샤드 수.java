/*
각 자리수를 나눠서 더해놓고 그걸로 x를 나눴을때 나눠떨어지면 true 아니면 false
*/


class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        
        char[] c = (x + "").toCharArray();
        int sum =0;
        for(char i: c){
            sum += i - '0';
        }
        
        answer = (x % sum == 0) ? true : false;
        
        
        return answer;
    }
}