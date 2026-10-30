/*
단어를 반복하며 돌아가면서 포함하고있으면 indexOf로 시작 부터 문자 길이만큼까지 자르기
.substring() 으로 슬라딩해서 새로운 문자열만들기
*/


class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] speaks = { "aya", "ye", "woo", "ma" };
        
        for(String word: babbling){
            String sentence = word;
            for(String speak : speaks){
                System.out.println(sentence);
                if(sentence.indexOf(speak) != -1){
                    sentence = sentence.substring(0,sentence.indexOf(speak)) + "-" +
                        sentence.substring(sentence.indexOf(speak) + speak.length() , sentence.length());
                }
            }
            if(sentence.replace("-","").equals("")){
                    answer++;
            }
        }
        return answer;
    }
    
}