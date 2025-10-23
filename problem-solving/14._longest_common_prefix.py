class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        for index in range(len(strs[0])):
          for word in strs:
            if index == len(word) or word[index] != strs[0][index]:
              return output
          output+=strs[0][index]
        return output   
    