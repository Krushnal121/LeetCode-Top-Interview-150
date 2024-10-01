import java.util.ArrayList;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rows=matrix.length,cols=matrix[0].length;
        int sizeidx=(rows*cols);
        ArrayList<Integer> arr= new ArrayList<Integer>();
        int startrow=0,startcol=0,endrow=rows-1,endcol=cols-1,idx=0;
        while(startrow<=endrow && startcol<=endcol){

            if(idx==sizeidx){break;}
            for(int i=startcol;i<=endcol;i++){
                arr.add(matrix[startrow][i]);
                idx++;
            }
            startrow++;
            if(idx==sizeidx){break;}
            for(int i=startrow;i<=endrow;i++){
                arr.add(matrix[i][endcol]);
                idx++;
            }
            endcol--;
            if(idx==sizeidx){break;}
            for(int i=endcol;i>=startcol;i--){
                arr.add(matrix[endrow][i]);
                idx++;
            }
            endrow--;
            if(idx==sizeidx){break;}
            for(int i=endrow;i>=startrow;i--){
                arr.add(matrix[i][startcol]);
                idx++;
            }
            startcol++;
        }
        return arr;
    }
}