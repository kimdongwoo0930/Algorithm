import java.util.*;

class Solution {
    public List<Integer> solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        
        int[][] p = {{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};
        
        int max_score = 0;
        
        for(int j = 0; j < p.length; j++){
            int score = 0;
            for(int i = 0; i < answers.length; i++){
                if(answers[i] == p[j][i % p[j].length]) score++;
            }
            
            if(max_score < score){
                max_score = score;
                answer.clear();
                answer.add(j+1);
            }
            else if(max_score == score){
                answer.add(j+1);
            }
        }   
        return answer;
    }
}