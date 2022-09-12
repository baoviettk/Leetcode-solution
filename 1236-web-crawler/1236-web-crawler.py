# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited={startUrl}
        q=deque([startUrl])
        
        while q:
            cur=q.popleft()
            urls=htmlParser.getUrls(cur)
            cur_dom=self.getDomain(cur)
            for u in urls:
                if u in visited or cur_dom!=self.getDomain(u): continue
                q.append(u)
                visited.add(u)
            
        return list(visited)
    
    def getDomain(self, url:str):
        return url.split('http://')[1].split('/')[0]