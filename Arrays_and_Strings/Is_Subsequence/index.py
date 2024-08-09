class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length=len(s)
        i=0
        if s=="":
            return True
        for ch in t:
            if s[i]==ch:
                i=i+1
                if i==length:
                    break
        if i==length:
            return True
        else:
            return False      