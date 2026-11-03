import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length - 1];
        
        if(arr.length == 1) return new int[] {-1};
        
        int min = 999999;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < min){
                min = arr[i];
            }
        }
        
         int idx = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == min) continue; 
            
            answer[idx++] = arr[i]; 
        }
        

        return answer;
    }
}