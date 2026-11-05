/*
첫번쨰 요소는 항상1이고
두번쨰부터 1번 음식 2번음식 3번음식 순서다
2로 나누고 목을 사용해야한다.
*/
import java.util.*;


class Solution {
    public String solution(int[] food) {
        String str1 = "";
        String str2 = "";
        
        for(int i = 1; i< food.length; i++){
            int k = (food[i] - (food[i] % 2)) / 2;
            str1 += String.valueOf(i).repeat(k);
            str2 = String.valueOf(i).repeat(k) + str2;
        }
        
        return str1 + "0" + str2 ;
    }
}