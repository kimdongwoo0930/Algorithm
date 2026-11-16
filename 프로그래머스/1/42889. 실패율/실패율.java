/*
실패율 = 클리어 못한 수 / 도달한 수 

스테이지 개수 : N
사용자들의 레벨들 : stages[]
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호를 정렬
*/
import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] list = new int[N+2];
        Map<Integer, Double> stage  = new HashMap<>();
        
        
         for(int i = 0; i < stages.length ; i++){
             list[stages[i]]++;
         }
        
        int members = stages.length;
        for(int i = 1; i <= N; i++){
            double fail = (members == 0) ? 0 : (double) list[i] / members;
            stage.put(i, fail);
            members -= list[i];
        }
        
        
        List<Map.Entry<Integer, Double>> lists = new ArrayList<>(stage.entrySet());
        
        
        lists.sort((a, b) -> {
            if (Double.compare(a.getValue(), b.getValue()) == 0) {
                return a.getKey() - b.getKey();           
            }
            return Double.compare(b.getValue(), a.getValue()); 
        });
        
        int[] answer = new int[lists.size()];
        for (int i = 0; i < lists.size(); i++) {
            answer[i] = lists.get(i).getKey();
        }
        
        
        
        return answer;
    }
}