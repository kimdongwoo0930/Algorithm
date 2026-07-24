/**
x만존재한다. 이러면 +로 나눠서 계산 split이 되나?
+만으로 하는거지 
*/
import java.util.*;
class Solution {
    public String solution(String polynomial) {
        String[] terms = polynomial.split(" \\+ ");
        int cntx = 0;
        int cnt = 0;
        // System.out.print(Arrays.toString(terms));
        for(String term: terms){
            if(term.contains("x")){
                term = term.replace("x","");
                cntx = term.isEmpty() ? cntx + 1 : cntx + Integer.parseInt(term);
            }
            else{
                cnt += Integer.parseInt(term);
            }
        }
        String answer = "";
        if(cnt > 0 && cntx > 0){
            answer = (cntx == 1) ? "x + " + cnt : cntx + "x + " + cnt;
        }
        else if (cnt == 0){
            answer = (cntx == 1) ? "x" : cntx + "x";
        }
        else if (cntx == 0){
            answer = Integer.toString(cnt);
        }
        
        return answer;
    }
}