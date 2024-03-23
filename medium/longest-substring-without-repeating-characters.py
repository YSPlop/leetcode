class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1 

        current_position = 1
        substring = ""
        max_len = 0