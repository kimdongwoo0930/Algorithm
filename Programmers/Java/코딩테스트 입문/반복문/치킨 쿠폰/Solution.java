
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

    // 제출할 땐 이 아래는 지우고 solution만 붙여넣기
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.solution(100));   // 기대값 11
        System.out.println(s.solution(1081));  // 기대값 120

        // 경계값도 확인해볼 것
        System.out.println(s.solution(0));     // 기대값 0
        System.out.println(s.solution(9));     // 기대값 0
        System.out.println(s.solution(10));    // 기대값 1
    }
}
