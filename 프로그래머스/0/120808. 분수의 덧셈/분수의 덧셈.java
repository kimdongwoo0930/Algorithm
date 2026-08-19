// 최소 공배수 구하는 공식

// int x = a,y = b,temp;
//         while(y != 0){
//             temp = y;
//             y = x % y;
//             x = temp;
//         }



/**
최소 공배수를 먼저 구해야한다.
로직 : a x b / 최대 공약수

*/
class Solution {
    public int[] solution(int number1, int denom1, int number2, int denom2) {
        
        int A = cal(denom1,denom2);
        // 분모
        int under = denom1 * denom2 / A;
        
        A = under / denom1;
        int B = under / denom2;
        
        // 분자를 구해야지
        int upper = number1 * A + number2 * B;
        
        // 약분이 되는지 확인해야지.
        
            A = cal(under,upper);
            upper /= A;
            under /= A;
        
        
    
        int[] answer = {upper, under };
        return answer;
    }

    public Integer cal(int a, int b){
            int x = a,y = b,temp;
            while(y != 0){
                temp = y;
                y = x % y;
                x = temp;
            }

            return x;
    }
    
}