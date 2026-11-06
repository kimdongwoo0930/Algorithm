/*
i번 부터 j번까지 짜르고 
정렬하고
k번쨰 숫자를 모은걸 내면된다.
*/

import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i = 0 ; i < commands.length ; i++){
            int[] arr = Arrays.copyOfRange(array,commands[i][0] - 1,commands[i][1]);
            Arrays.sort(arr);
            answer[i] = arr[commands[i][2] - 1]; 
        }
        
        return answer;
    }
}