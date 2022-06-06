class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i=0
        j=0
        arr=[]
        while i<len(firstList) and j< len(secondList):
            if self.isIntersected(firstList[i],secondList[j]):
                arr.append([max(firstList[i][0],secondList[j][0]),                                min(firstList[i][1],secondList[j][1])])
            if firstList[i][1]>secondList[j][1]:
                j+=1
            elif firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                i+=1
                j+=1
        return arr
        
    def isIntersected(self, interval1, interval2):
        if ((interval1[0]>=interval2[0]) and (interval1[0]<=interval2[1])) or ((interval2[0]>=interval1[0]) and (interval2[0]<=interval1[1])):
            return True
        return False