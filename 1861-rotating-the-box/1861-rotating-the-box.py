class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        MAX_X,MAX_Y=len(box[0]), len(box)
        for y in range(MAX_Y):
            cur_x=MAX_X-1
            for x in range(MAX_X-1,-1,-1):
                if box[y][x]=='#':
                    box[y][x]='.'
                    box[y][cur_x]='#'
                    cur_x-=1
                elif box[y][x]=='*':
                    cur_x=x-1
        return zip(*box[::-1]) 