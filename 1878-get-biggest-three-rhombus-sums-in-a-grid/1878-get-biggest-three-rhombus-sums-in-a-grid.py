class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        MAX_Y, MAX_X = len(grid), len(grid[0])
        li = []
        for i in range(MAX_Y):
            for j in range(MAX_X):
                li.append(grid[i][j])
                top = grid[i][j]
                d=1
                while j - d > -1 and j + d < MAX_X and i + d < MAX_Y:
                    l = j-d
                    r = j+d
                    y = i+d
                    top += grid[y][l] + grid[y][r]
                    bot = 0
                    while True:
                        l += 1
                        r -= 1
                        y += 1
                        if l == -1 or r == MAX_X or y == MAX_Y:
                            break

                        if l == r:
                            bot += grid[y][l]
                            li.append(top + bot)
                            break
                        bot += grid[y][l] + grid[y][r]
                    d+=1
        li = list(set(li))
        li.sort(reverse=True)
        return li[:3]
                