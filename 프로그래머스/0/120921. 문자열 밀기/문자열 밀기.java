/**
한칸씩 계속 밀면된다. 한마디로 큐로 앞에 뺴고 뒤로 넣는거다.
*/


class Solution {
    public int solution(String A, String B) {
        
        int answer = 0;
        String shift = A;
        for(int i = 0; i< A.length() ; i++){
            if(shift.equals(B)) {
                return answer;
            }
            String last = shift.substring(shift.length() - 1);
            String after = shift.substring(0,shift.length() - 1);
            shift = last + after;
            answer++;
            
        }
        return -1;
    }
}