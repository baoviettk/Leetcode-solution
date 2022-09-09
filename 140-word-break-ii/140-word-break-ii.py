class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp={}
        word_set=set(wordDict)
        
        def break_word(sub):
            if sub in dp:
                return dp[sub]
            result=[]
            for i in range(len(sub)):
                if sub[:i+1] in word_set:
                    prefix=sub[:i+1]
                    if prefix==sub:
                        result.append(prefix)
                    else:
                        rest=break_word(sub[i+1:])
                        for s in rest:
                            result.append(prefix + " "+ s)
            dp[sub]=result
            return result
            
            
        return break_word(s)