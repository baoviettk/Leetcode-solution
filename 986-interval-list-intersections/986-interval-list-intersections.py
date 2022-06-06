class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i=0
        j=0
        arr=[]
        while i<len(firstList) and j< len(secondList):
            low= max(firstList[i][0],secondList[j][0])
            high= min(firstList[i][1],secondList[j][1])
            if low<=high:
                arr.append([low,high])
            if firstList[i][1]>secondList[j][1]:
                j+=1
            elif firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                i+=1
                j+=1
        return arr
        