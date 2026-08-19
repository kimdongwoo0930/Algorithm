/*
선의 처음과 끝을 리스트로 준다.
선이 겹치는 부분의 길이의 합을 구하면 된다.
풀이법:
    1. A의 마지막과 B의 첫번째를 비교해서 A가 B보다 크면 그 둘을 뺀걸 더하면 된다.
    
    틀렸다.
    
    선분은 연속적으로 존재하지않는다.
    
    리스트를 -100부터 100까지 만들어두고
    리스트부터 한개씩 1씩더해서 만약 2가 넘어가는게 몇개인지 구하면된다.
    
*/


class Solution {
    public int solution(int[][] lines) {
        
        int[] count = new int[201];
        for(int[] line : lines){
            int A = line[0] + 100;
            int B = line[1] + 100;
            
            for(int i = A; i < B ; i++){
                count[i] += 1;
            }
        }
        int answer=0;    
        for (int c : count) {
            if (c >= 2) answer++;
        }
    
        return answer;
    }
}