class Solution {
    boolean solution(String s) {
        boolean answer = true;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
        s = s.toLowerCase();
        
        int p = 0, y = 0;
        
        for(char c: s.toCharArray()){
            if(c == 'p') p += 1;
            else if (c == 'y') y += 1;
        }
        
        
        answer = (p == y) ? true : false;
        

        return answer;
    }
}