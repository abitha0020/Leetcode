class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value = {
            "I" : 1,
            "V":5,
            "X": 10,
            "L": 50,
            "C":100,
            "D":500,
            "M": 1000
        } 
        s=s.replace("IV","IIII").replace("IX","VIIII")
        s=s.replace("XL","XXXX").replace("XC","LXXXX")
        s=s.replace("CD","CCCC").replace("CM","DCCCC")  
        num=0
        for c in s:
            num=num+value[c]
        return num  