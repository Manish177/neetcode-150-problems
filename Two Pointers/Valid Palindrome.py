class Solution:
    def isPalindrome(self, s: str) -> bool:
        str="".join(c.lower() for c in s if c.isalnum())
        str1=str[::-1]
        return str==str1
