/*
사과의 최대점수는 k
박스에 들어가야하는 개수는 4개

score를 오른차순을 해두고 m개씩 이동하면서 뒤에서 m번째 꺼와 m을 곱한다.
남은 사과들은 어차피 m을 뺐을때 0보다 작아지기때문애 자동으로 빠진다.
*/
import java.util.*;


class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        Arrays.sort(score);
        
        for(int i = score.length - m ; i >= 0; i -= m){
            answer += score[i] * m;
        }
        
        return answer;
    }
}