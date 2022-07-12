class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        arr=[]
        i_arr=[0]*len(nums)
        len_arr=[]
        for i in range(len(nums)):
                heappush(heap,[nums[i][i_arr[i]],i])
                i_arr[i]+=1
                len_arr.append(len(nums[i]))
                
        while len(heap)>0:
            val,index=heappop(heap)
            arr.append([val,index])
            if i_arr[index]<len_arr[index]:
                heappush(heap,[nums[index][i_arr[index]],index])
                i_arr[index]+=1
        left, right=0,0
        dic=[0]*len(nums)
        dic[arr[left][1]]+=1
        while not self.checkValid(dic):
            right+=1
            dic[arr[right][1]]+=1
            
        min_range=arr[right][0]-arr[left][0]
        min_left,min_right=arr[left][0],arr[right][0]
        dic[arr[right][1]]-=1
        for i in range(right,len(arr)):
            dic[arr[i][1]]+=1
            right=i
            while True:
                if dic[arr[left][1]]>1:
                    dic[arr[left][1]]-=1
                    left+=1
                    
                else:
                    break
            curr_min= arr[right][0]-arr[left][0]
            if min_range>curr_min:
                min_range=curr_min
                min_left= arr[left][0]
                min_right=arr[right][0]
        return [min_left,min_right]
    
    def checkValid(self, dic):
        for i in range(len(dic)):
            if dic[i]==0:
                return False
        return True