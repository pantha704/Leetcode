class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] or ""
        for string in strs[1:] :
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix 
