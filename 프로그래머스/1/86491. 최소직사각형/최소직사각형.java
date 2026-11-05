/*
10 7
12 7
15 8
15 8
15 8
*/

class Solution {
    public int solution(int[][] sizes) {
        int max = Math.max(sizes[0][0],sizes[0][1]);
        int min = Math.min(sizes[0][0],sizes[0][1]);
        
        for(int[] nums : sizes){
            if(max < Math.max(nums[0],nums[1])){
                max = Math.max(nums[0],nums[1]);
            }
            if(min < nums[0] && min < nums[1]){
                min = Math.min(nums[0],nums[1]);
            }
        }
        
        return max * min;
    }
}