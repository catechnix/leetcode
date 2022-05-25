s1 = "abcadbcbb"
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(set(s)) == len(s):                       # Checking if the string is unique
            return len(s)
        substring = ''
        maxLen = 1
        for i in s:
            if i not in substring:                      # If given character is not in substring we are generating, we add it to the substring
                substring = substring + i
                maxLen = max(maxLen, len(substring))    # We update the maxlength if our substring is longer than the current max.
            else:                                       # Else, if the character is already part of the substring, we need to break the flow
                substring = substring.split(i)[1] + i   # And create a new substring from that point onwards and this new substring is build from the next character. Process repeats till the loop ends.
                print (substring.split(i)[1])
        
        return maxLen
        

s = Solution()
print(s.lengthOfLongestSubstring(s1))