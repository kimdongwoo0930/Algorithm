/*
i 고정 j 증가 끝을 만나면 j 고정 i 증가 i가 끝을만나면 i고정 j감소
*/

import java.util.*;

class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n]; // 리스트를 0으로 채움
        
        int num = 1;
        int minX = 0, maxX = n - 1, minY = 0, maxY = n - 1;
        
        
        while(num <= n*n){
            for(int x=minX; x<= maxX; x++){
                answer[minY][x] = num;
                num++;
            }
            minY++;
            for(int y= minY; y <= maxY; y++ ){
                answer[y][maxX] = num;
                num++;
            }
            maxX--;
            for(int x = maxX; x >= minX; x--){
                answer[maxY][x] = num;
                num ++;
            }
            maxY--;
            for(int y= maxY; y >= minY; y-- ){
                answer[y][minX] = num;
                num++;
            }
            minX++;
        }

        
        
        return answer;
    }
}