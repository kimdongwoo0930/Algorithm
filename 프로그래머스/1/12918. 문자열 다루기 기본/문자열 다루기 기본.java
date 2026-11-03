class Solution {
    public boolean solution(String s) {
        if (s.length() != 4 && s.length() != 6) {
            return false;
        }
        
        
        char[] list = s.toCharArray();
        
        for(char c: list){
            if(!Character.isDigit(c)) return false;
        }
        
        return true;
    }
}