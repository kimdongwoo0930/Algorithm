class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for(int i = 0; i < n; i++){
            // 2개를 가져와 2진수로 바꾸고 한자리씩 비교후 
            String num1 = two(arr1[i], n);
            String num2 = two(arr2[i], n);
            answer[i] = "";
            for(int j = 0 ; j < n; j++){
                if(num1.charAt(j) == '1' || num2.charAt(j) == '1'){
                    answer[i] += "#";
                }
                else{
                    answer[i] += " ";
                }
            }
        }
        
        return answer;
    }
    
    
    private String two(int num,int n){
        String anw = "";
        for(int i = 0; i < n; i++){
            anw =  num % 2 + anw;
            num /= 2;
        }
        return anw;
    }
}


