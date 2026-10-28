/*
1. 주사위 4개가 모두 P로 같다면 1111x P 점
2. 주사위 3개가 P로 같고 나머지 1개의 숫자가 Q일때 (10 x p + q)^2
3. 
*/
import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 1;
        int[] list = {a, b, c, d};
        
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < 4; i++){
            int key = list[i];
            if(!map.containsKey(key)){
                map.put(key,0);
            }
            map.put(key, map.get(key) + 1);
            // map.put(key, map.getOrDefault(key, 0) + 1); 같은 뜻
        }
        int size = map.size();
        
        switch(size){
            case 1:
                answer = a * 1111;
                break;
            case 2:
                // 3 - 1일때랑 2-2일떄를 구해야함
                int p = 0 , q = 0;
                for (int key : map.keySet()) {
                    if (p == 0) p = key;
                    else q = key;
                }
                if(map.get(p) != 2){
                  int x = (map.get(p) == 3) ? (10 * p + q) : (10 * q + p);
                    answer = x * x;
                }else{
                    answer = (p + q) * Math.abs(p - q);
                }
                break;
            case 3:
                for(int key : map.keySet()){
                        if(map.get(key) == 1){
                            answer *= key;
                        }
                }
                break;
                
            case 4:
                int min = 6;
                for(int key : map.keySet()){
                        if(min > key) min = key; 
                }
                answer = min;
                break;
        }
        
        return answer;
    }
}