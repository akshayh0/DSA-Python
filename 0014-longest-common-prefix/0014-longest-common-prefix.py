class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as the initial baseline prefix
        prefix = strs[0]
        
        # Compare the prefix with every other string in the list
        for s in strs[1:]:
            # Shorten the prefix until it matches the start of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix
