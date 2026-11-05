/*
여기서 모든 합을 구하고 결국 set을 사용해보게된다.
*/
import java.util.*;

class Solution {
    public List<Integer> solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        
        for(int i = 0; i< numbers.length - 1;i++){
            for(int j = i + 1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        List<Integer> answer = new ArrayList<>(set);
        
        Collections.sort(answer);
        
        
        return answer;
    }
}