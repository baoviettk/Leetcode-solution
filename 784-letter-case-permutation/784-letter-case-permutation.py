class Solution(object):
    def letterCasePermutation(self, s):
        stack, result=[],[]
        n=len(s)
        
        
        def bfs(i):
            if len(stack)==n:
                result.append("".join(stack))
                return
            if s[i].isnumeric():
                stack.append(s[i])
                bfs(i+1)
                stack.pop()
            else:
                stack.append(s[i])
                bfs(i+1)
                stack.pop()
                
                stack.append(swapcase(s[i]))
                bfs(i+1)
                stack.pop()
                
            return
                             
                             
        
        bfs(0)
        return(result)