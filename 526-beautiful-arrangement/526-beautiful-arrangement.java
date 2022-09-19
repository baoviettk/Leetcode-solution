class Solution {
    int result=0;
    public int countArrangement(int n) {
        int[] arr= new int[n];
        for (int i=0;i<n;i++){
            arr[i]=i+1;
        }
        check(arr,n,0);
        return result;
            
    }
    
    public void check(int[] arr, int n, int j){
        if (j==n){
            result++;
            return;
        }
        for (int i=j;i<n;i++){
            swap(arr,i,j);
            if (arr[j]%(j+1)==0 || (j+1)%arr[j]==0){
                check(arr,n,j+1);
            }
            swap(arr,i,j);

        }
    }
    
    public void swap(int[]arr,int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    
    }
}