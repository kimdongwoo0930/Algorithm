/*
지금 그냥 signs에서 true면 양수 false면 음수
동시에 꺼면서 부호를 붙여주고 그걸 더하면 끝아님?
*/


class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        
        for(int i = 0; i < absolutes.length; i++){
            answer += (signs[i]) ? absolutes[i] : -1 * absolutes[i];
        }
        
        return answer;
    }
}