class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
haystack = input("Enter a string : ")
needle = input("Enter a string to search : ")

solution = Solution()
print(solution.strStr(haystack,needle))