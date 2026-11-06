import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
         List<String> l1 = new ArrayList<>(Arrays.asList(cards1));
        List<String> l2 = new ArrayList<>(Arrays.asList(cards2));
        
        for(String word : goal){
            if(!l1.isEmpty() && l1.get(0).equals(word)){
                l1.remove(0);
            }
            else if(!l2.isEmpty() && l2.get(0).equals(word)){
                l2.remove(0);
            }
            else{
                return "No";
            }
        }
        return "Yes";
    }
}