import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        
        int[] answer = numlist.clone();
        int len = answer.length - 1;
        
        for(int i = 0; i< len ; i++){
            for(int j = 0; j < len; j++){
                int distA = Math.abs(answer[j] - n);
                int distB = Math.abs(answer[j+1] - n);
                // 사이거리가 다를때 
                boolean Swap;
                if(distA != distB){
                    Swap = distA > distB;
                }
                else{
                    Swap = answer[j] < answer[j+1];
                }
                
                if(Swap){
                    int temp = answer[j];
                    answer[j] = answer[j+1];
                    answer[j+1] = temp;
                }
            }
        }
        return answer;
       // 이게 Array의 Sort를 이용한것이고 
//         Integer[] arr = new Integer[numlist.length];
//         int i = 0;
//         for(int j: numlist){
//             arr[i] = j;
//             i++;
//         }
        
//         Arrays.sort(arr, (a, b) -> {
//             int distA = Math.abs(a - n);
//             int distB = Math.abs(b - n);
//             if (distA != distB) {
//                 return distA - distB;
//             }
//             return b - a;
//         });
        
//         return arr;
        
        
        
    }
}