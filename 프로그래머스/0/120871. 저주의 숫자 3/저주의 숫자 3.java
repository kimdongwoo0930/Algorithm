/**
1부터 n까지의 3이 들어간 숫자 개수를 구하는지
그럼 먼저 숫자를 문자로 바꾸고 거기에 3이 포함된건지 찾아야지

아니네 이거 앞에서부터 해야 알수가 있구나 몇인지 
*/

import java.util.*;

class Solution {
    public int solution(int n) {
        int num = 0;
        int count = 0;
        
        while (count < n) {
            num++;
            String str = Integer.toString(num);
            if (!(str.contains("3") || num % 3 == 0)) {
                count++;
            }
        }
        
        return num;
    }
}