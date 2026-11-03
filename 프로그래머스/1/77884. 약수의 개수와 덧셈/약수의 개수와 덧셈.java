

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        for(int j = left; j <= right; j++){
            answer += (measure(j) % 2 == 0) ? j : -1 * j;
        }
        
        
        return answer;
    }
    
    
    
    public int measure(int num){
    int count = 0;
    for(int i = 1; i <= num ; i++){
        if(num % i == 0) count++;
    }
    return count;
}
}

