class Solution {
    public int maxResult(int[] nums, int k) {
        Deque<Integer> q =new ArrayDeque<>(); //store index
        int n = nums.length;
        q.offer(0);
        for (int i=1;i<n;i++){
            nums[i]+=nums[q.peekFirst()];
            while (!q.isEmpty() && nums[q.peekLast()]<=nums[i]){
                q.pollLast();
            }
            q.offerLast(i);
            if (i-q.peekFirst()>=k){
                q.pollFirst();
            }
        }
        return nums[n-1];
        
    }
}