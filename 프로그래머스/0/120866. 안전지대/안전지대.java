/**
설마 한칸씩 넘어가면서 근처 8칸에 지뢰가 있는지 확인해야하는거 같은데
*/

class Solution {
    public int solution(int[][] board) {
        // 8칸을 확인하기위해서는 2중 for문으로가야한다.
        
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        int n = board.length;
        
        int answer = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 1) continue;
                boolean result = true;
                for(int d = 0; d < 8; d++){
                    int x = i + dx[d];
                    int y = j + dy[d];
                    
                    if(x < 0 || x >= n || y < 0 || y >= n) continue;
                    if(board[x][y] == 1){
                        result = false;
                        break;
                    }
                }
                if(result) answer++;
            }
        }
        
        
        
        return answer;
    }
}