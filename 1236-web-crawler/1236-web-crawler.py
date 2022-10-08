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
        q=collections.deque([startUrl])
        visited={startUrl}
        start=self.getHost(startUrl)
        while q:
            cur=q.popleft()
            nxt=htmlParser.getUrls(cur)
            for s in nxt:
                if s not in visited and self.getHost(s)==start:
                    visited.add(s)
                    q.append(s)
        
        return list(visited)
    
    def getHost(self, url)-> str:
        return url.split("//")[1].split("/")[0]
    