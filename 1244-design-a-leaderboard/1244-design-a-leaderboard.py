class Leaderboard:

    def __init__(self):
        self.board={}
    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId]=self.board.get(playerId,0) + score

    def top(self, K: int) -> int:
        heapK=heapq.nlargest(K,self.board.values())
        return sum(heapK)

    def reset(self, playerId: int) -> None:
        del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)