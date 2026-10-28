import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = arr;
        for (int i = 0; i < query.length; i++) {
            int q = query[i];
            if (i % 2 == 0) {
                // 짝수 인덱스: q번 뒷부분 버림 (q 포함해서 앞쪽만 남김)
                answer = Arrays.copyOfRange(answer, 0, q + 1);
            } else {
                // 홀수 인덱스: q번 앞부분 버림 (q 포함해서 뒤쪽만 남김)
                answer = Arrays.copyOfRange(answer, q, answer.length);
            }
        }
        return answer;
    }
}