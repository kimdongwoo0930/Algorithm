class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] speak = {"aya","ye","woo","ma"};
        
        // 하나씩 가져온다.
        // contains를 확인후 비교 그리고 문자열에서 제거 및 다음 문자열로 비교
        
        for(int i = 0; i < babbling.length; i++){
            String word = babbling[i];
            
            
            boolean invalid = false;
            for (String s : speak) {
                if (word.contains(s + s)) {
                    invalid = true;
                    break;
                }
            }
            if (invalid) continue;
            
            for(String s : speak){
                    word = word.replace(s," ");
            }
            if(word.trim().isEmpty()){
                answer++;
            }
            
            
        }
        
        return answer;
    }
}