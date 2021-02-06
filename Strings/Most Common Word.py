# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/most-common-word/

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph=paragraph.lower()
        for i in banned:
            paragraph=paragraph.replace(i,' ')
        paragraph=paragraph.replace("!",' ')
        paragraph=paragraph.replace("?",' ')
        paragraph=paragraph.replace(",",' ')
        paragraph=paragraph.replace("'",' ')
        paragraph=paragraph.replace(";",' ')
        paragraph=paragraph.replace(".",' ')
        
        x=paragraph
        a=x.split(' ')
        
        d={}
        for i in a:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        print(d)
        
        mx=0
        ans=''
        for i in d:
            if d[i]>mx and i!='':
                ans=i
                mx=d[i]
       
        return(ans)
        