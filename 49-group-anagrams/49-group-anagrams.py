class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        
        for s in strs:
            has=[0]*26
            for c in s:
                has[ord(c)-ord("a")]+=1
            result[tuple(has)].append(s)
        
        return result.values()
            