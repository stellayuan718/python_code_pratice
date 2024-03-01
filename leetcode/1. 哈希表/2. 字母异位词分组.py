class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashtable = {}

        for word in strs:
            sort_word = ''.join(sorted(word))

            if sort_word in hashtable:
                hashtable[sort_word].append(word)

            else:
                hashtable[sort_word] = [word]

        return list(hashtable.values())

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
a = s.groupAnagrams(strs)
print(a)