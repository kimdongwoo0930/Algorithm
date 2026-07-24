/**
제일먼저 모두의 평균을 구해서 리스트에 넣고
자기보다 큰 개수를 각 구한다.
*/
import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[][] score) {
        ArrayList<Double> avgs = new ArrayList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int[] list : score){
            avgs.add((list[0] + list[1]) / 2.0 );
        }
        for(int[] list : score){
            double avg = (list[0] + list[1]) / 2.0;
            int cnt = 0;
            for(double num : avgs){
                if(num > avg) cnt++;
            }
            answer.add(++cnt);
        }
        
        
        return answer;
    }
}