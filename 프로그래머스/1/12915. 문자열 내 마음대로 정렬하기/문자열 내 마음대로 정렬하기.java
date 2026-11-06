/*
그냥 
생각보면 사실 Map으로 a ~ b까지 각자 list만들어두고 각 리스트를 sort하고 앞에서부터 정렬하면 끝
*/

import java.util.*;

class Solution {
    public List<String> solution(String[] strings, int n) {
        List<String> answer = new ArrayList<>();
        
        Map<Character,List<String>> book = new HashMap<>();
        
        for(String s: strings){
            char key = s.charAt(n);
            if(!book.containsKey(key)) book.put(key, new ArrayList<>(List.of(s)));
            else{
                book.get(key).add(s);
            }
            
        }
        // 이제 앞에서부터 가져오고 list를 매번 sort하고 연결하면 끝.
        for(char i = 'a'; i <= 'z' ; i ++){
            if(book.containsKey(i)){
                List<String> list = book.get(i);
                Collections.sort(list);
                answer.addAll(list);
            }
        }
        System.out.println(book);
        System.out.println(answer);
        
        
        
        return answer;
    }
}