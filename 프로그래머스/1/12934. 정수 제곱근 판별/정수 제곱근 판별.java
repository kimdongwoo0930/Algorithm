

class Solution {
    public long solution(long n) {
        long num = (long) Math.sqrt(n);
        
        
        long answer = -1;
        if(num * num == n){
            answer = (num+1)  * (num+1);
        }
        
        return answer;
    }
}