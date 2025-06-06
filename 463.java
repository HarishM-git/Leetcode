class Solution {
    public int islandPerimeter(int[][] x) {
        int c=0;
        int z=0;
        for(int i=0;i<x.length;i++){
            for(int j=0;j<x[0].length;j++){
                // if(x[i][j]==1){
                //    try{
                //     if(x[i-1][j]==0){
                //         c+=1;
                //     }
                //    }
                //    catch (Exception e) {
                //     c+=1;
                //    }
                //    try{
                //     if(x[i+1][j]==0){
                //         c+=1;
                //     }
                //    }
                //    catch (Exception e) {
                //     c+=1;
                //    }
                //    try{
                //     if(x[i][j-1]==0){
                //         c+=1;
                //     }
                //    }
                //    catch (Exception e) {
                //     c+=1;
                //    }
                //    try{
                //     if(x[i][j+1]==0){
                //         c+=1;
                //     }
                //    }
                //    catch (Exception e) {
                //     c+=1;
                //    }
                // }
                else{
                    z=1;
                }
               
            }
        }
        if(z==0){
            return ((x.length)+(x[0].length))*2;
        }
        return c;
    }
}
