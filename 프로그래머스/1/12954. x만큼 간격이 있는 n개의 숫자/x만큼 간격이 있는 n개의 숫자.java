class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        
        
        for(long i = x ; (x > 0) ? i <= (long) x * n : i >= (long) x * n  ; i += x){
            if(x == 0) return answer;
            answer[(int) (i / x) - 1] = i;
        }
        
        
        return answer;
    }
}