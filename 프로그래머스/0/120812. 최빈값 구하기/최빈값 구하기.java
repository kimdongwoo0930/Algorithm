/**
가장 자주나오는 값을 표시하는거다.
하지만 최빈값이 여러개인경우 -1 아닌경우는 1로 그숫자를 표시한다.

리스트를 쭉 돌면서 개수를 구해야하나 파이썬이라면 그냥 개수로 구했을꺼같지만 
이러면 개수가 가장큰걸 저장해두고 다음값이 몇개인지 구해서 나온값을 
최빈값보다 크면 변경 근데 만약 개수가 같으면 어떻하지?

*/
import java.util.*;
class Solution {
    public int solution(int[] array) {
        // 1. 방문한곳을 저장
        // 2. 개수값을 저장
        // 3. 최대값
        // 4. 최대값의 숫자
        List<Integer> arrayList = new ArrayList<>();
        for (int num : array) {
            arrayList.add(num);
        }
        
        List<Integer> visited = new ArrayList<>();
        List<Integer> counts = new ArrayList<>();
        
        int maxcount = 0;
        int maxnum = 0;
        
        
        // 1. 개수를 구함
        // 2. 만약 최대개수로 구했던거보다 크면 갱신
        // 3. 마지막에 최빈값수가 카운터에 1개보다 크면 -1
        // 4. 만약 최빈값이 1개면 맥스넘버가 답이다.
        for(int num : array){
            if(!visited.contains(num)){
                // 계산한적없다면야
                 int count = Collections.frequency(arrayList, num);
                if(maxcount < count){
                    maxcount = count;
                    maxnum = num;
                }
                counts.add(count);
                visited.add(num);
            }
        }
        if(Collections.frequency(counts, maxcount) < 2){
            return maxnum;
        }
        else{
            return -1;
        }
    }
}