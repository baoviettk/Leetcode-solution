class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        min_capital=[]
        max_profit=[]
        current_w=w
        for i in range(len(capital)):
            heapq.heappush(min_capital,(capital[i],i))
        for _ in range(k):
            while min_capital and min_capital[0][0]<=current_w:
                cur_cap,i=heapq.heappop(min_capital)
                heapq.heappush(max_profit,(-profits[i]))
            if not max_profit:
                break
            current_w+=-heapq.heappop(max_profit)
            
        return current_w
        