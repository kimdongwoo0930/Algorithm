/**
등비 또는 등차인 리스트를 판단하고 다음에 올 숫자를 구하면된다.
*/

class Solution {
    public int solution(int[] common) {
        int answer = 0;
        // 제일먼저 리스트를 보며 등비인지 등차인지 판단을 해야한다.
        // 등차인지 판단후 아니라면 등비이기때문에 
        // 2번째에서 1번쨰 뺀거와 3번쨰에서 2번째꺼 뺸걸 같다고하면 등차
        
        if(common[1] - common[0] == common[2] - common[1]){
            // 등차
            // 공차 구하기
            int cha = common[1] - common[0];
            
            answer = common[common.length - 1] + cha;
        }
        else{
            // 등비
            // 공비 구하기
            int bi = common[1] / common[0];
            
            answer = common[common.length - 1] * bi;
        }
        
        return answer;
    }
}