class Trie:
    def __init__(self):
        self.children={}
        self.isEnd=False
    def addWord(self, word:str) -> None:
        current=self
        for w in word:
            if w not in current.children:
                current.children[w]=Trie()
            current=current.children[w]
        current.isEnd=True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.numFind=len(words)
        LEN_X, LEN_Y= len(board), len(board[0])
        result= []
        root=Trie()
        for w in words:
            root.addWord(w)
            
        def dfs(x,y,cur,w):
            if self.numFind==0:
                return
            if cur.isEnd:
                result.append(w)
                cur.isEnd=False
                self.numFind-=1
            if x<0 or y<0 or x== LEN_X or y == LEN_Y or board[x][y] not in cur.children:
                return
            temp=board[x][y]
            board[x][y]="#"
            w+=temp
            cur=cur.children[temp]
            dfs(x-1,y,cur,w)
            dfs(x+1,y,cur,w)
            dfs(x,y-1,cur,w)
            dfs(x,y+1,cur,w)
            board[x][y]=temp
        
        for x in range(LEN_X):
            for y in range(LEN_Y):
                dfs(x,y,root,"")
        return result