/**
1081장 있다
108번 시키고
108장 추가하고
10번 시키고
10장 추가
9장
109장
원래 가지고있던 쿠폰수가있찌
*/


class Solution {
    public int solution(int chicken) {
        int coupon = chicken;
        int answer = 0;
        while(coupon >= 10){
            answer += coupon / 10;
            coupon = coupon % 10 + coupon / 10;
        }
        return answer;
    }
}