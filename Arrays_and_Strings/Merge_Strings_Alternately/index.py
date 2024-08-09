class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1=len(word1)
        len2=len(word2)
        if len1<=len2:
            length=len1
        else:
            length=len2  
        str1=""
        for i in range(length):
            str1+=word1[i]
            str1+=word2[i]
        while (len1>length):
            str1+=word1[length]
            length=length+1
        while (len2>length):
            str1+=word2[length]
            length=length+1
        return str1  