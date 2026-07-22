class Solution {
    public int solution(int n) {
        int num = 0;
        int count = 0;
        
        while (count < n) {
            num++;
            String str = Integer.toString(num);
            if (!(str.contains("3") || num % 3 == 0)) {
                count++;
            }
        }
        
        return num;
    }

    // 제출할 땐 이 아래는 지우고 solution만 붙여넣기
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.solution(15));  // 기대값 25
        System.out.println(s.solution(40));  // 기대값 76

        // 표에 나온 앞부분도 확인해볼 것
        System.out.println(s.solution(1));   // 기대값 1
        System.out.println(s.solution(3));   // 기대값 4
        System.out.println(s.solution(7));   // 기대값 10
    }
}
