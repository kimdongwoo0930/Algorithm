/*
지폐가 지갑에 들어가지 않는다면 반으로 접어야한다
- 반으로 접을때 길이가 긴쪽부터 접는다
- 홀수일경우 접고 소수점은 날린다.

*/

import java.util.*;

class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        int wallet_min = Math.min(wallet[0],wallet[1]);
        int wallet_max = Math.max(wallet[0],wallet[1]);
        
        while(!(Math.max(bill[0],bill[1]) <= wallet_max &&
              Math.min(bill[0],bill[1]) <= wallet_min))  {
            if(bill[0] > bill[1]){
                bill[0] = bill[0] / 2;
            }
            else{
                bill[1] = bill[1] / 2;
            }
            answer++;
        }
        
        
        
        return answer;
    }
}