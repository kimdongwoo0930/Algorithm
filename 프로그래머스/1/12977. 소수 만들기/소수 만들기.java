/*
3개의 합들에서 소수를 구하면되면 2중 for문을 이용해 3개씩 더한값을 소수가 맞는지 아닌지 확인하는 함수를 제작후 넣는다.
*/

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        for(int k = 0; k < nums.length - 2; k++){
            for(int i = k + 1; i < nums.length - 1; i++){
                for(int j = i + 1; j < nums.length; j++){
                    int sum = nums[k] + nums[i] + nums[j];
                    if(isPrime(sum)) answer++;
                }
            }
        }
        
        return answer;
    }
    
    
    public boolean isPrime(int num){
        for(int i = 2; i <= Math.sqrt(num); i++ ){
            if(num % i == 0) return false;
        }
        return true;
    }
    
}