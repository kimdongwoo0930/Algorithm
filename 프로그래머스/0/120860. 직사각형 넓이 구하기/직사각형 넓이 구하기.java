import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        ArrayList<Integer> X = new ArrayList<>();
        ArrayList<Integer> Y = new ArrayList<>();
        
        for(int[] list : dots){
            if(!X.contains(list[0])) X.add(list[0]);
            if(!Y.contains(list[1])) Y.add(list[1]);
        }
        int answer = Math.abs(X.get(0) - X.get(1)) * Math.abs(Y.get(0) - Y.get(1));
        
    
        return answer;
    }
}