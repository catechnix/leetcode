"""
Reverse a string with spaces in the front and the end, and any spaces in between.
"""

import re
class Solution:
      
    def reverseWords(self, s: str) -> str:
        s2=""
        s.strip()  #remove space in the beginning and end
        s1=re.sub("\s+"," ",s)  #remove multiple spaces in the string
        list=s1.split(" ")   #change the string to a list
        list.reverse()   # reverse the list
        for w in list:
            s2 +=w + " "  #put list into a string
        
        return s2


s = "   Life    is good !     "

print(Solution().reverseWords(s))
