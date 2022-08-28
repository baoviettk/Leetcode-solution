class Solution(object):
    def intToRoman(self, num):
        sym=[[1000,'M'], [900,'CM'],[500,'D'],[400,'CD'], [100,'C'], [90,'XC'], [50,'L'],[40,'XL'],[10,'X'], [9,'IX'],[5,'V'], [4,'IV'], [1,'I']]
        
        i = 0
        result=''
        while num>0:
            [cur_num, cur_sym]=sym[i]
            count=num//cur_num
            result+=cur_sym*count
            num%=cur_num
            i+=1
            
        return result
        