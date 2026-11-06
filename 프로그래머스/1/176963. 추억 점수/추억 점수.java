import java.util.*;

class Solution {
    public List<Integer> solution(String[] name, int[] yearning, String[][] photo) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> points = new HashMap<>();
        for(int i = 0; i < name.length; i++){
            points.put(name[i],yearning[i]);
        }
        
        System.out.println(points);
        
        for(String[] names : photo){
            int point = 0;
            for(String nm : names){
                point += points.getOrDefault(nm,0);
            }
            answer.add(point); 
        }
         
        
        
        return answer;
    }
}