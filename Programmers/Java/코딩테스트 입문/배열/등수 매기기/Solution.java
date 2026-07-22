import java.util.Arrays;

/**
제일먼저 모두의 평균을 구해서 리스트에 넣고
자기보다 큰 개수를 각 구한다.
*/
import java.util.*;

/**
제일먼저 모두의 평균을 구해서 리스트에 넣고
자기보다 큰 개수를 각 구한다.
*/
import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[][] score) {
        ArrayList<Integer> sums = new ArrayList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int[] list : score){
            sums.add((list[0] + list[1]) / 2 );
        }
        for(int[] list : score){
            int avg = (list[0] + list[1]) / 2;
            int cnt = 0;
            for(int num : sums){
                if(num > avg) cnt++;
            }
            answer.add(++cnt);
        }
        
        
        return answer;
    }
    // 제출할 땐 이 아래는 지우고 solution만 붙여넣기
    public static void main(String[] args) {
        Solution s = new Solution();

        // 기대값 [1, 2, 4, 3]
        System.out.println(Arrays.toString(
                s.solution(new int[][] {{80, 70}, {90, 50}, {40, 70}, {50, 80}})));

        // 기대값 [4, 4, 6, 2, 2, 1, 7]
        System.out.println(Arrays.toString(
                s.solution(new int[][] {{80, 70}, {70, 80}, {30, 50}, {90, 100}, {100, 90}, {100, 100}, {10, 30}})));
    }
}
