class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if (len(str1) != len(str2)):
            return False

        table = {}

        for i in range(0, len(str1)):
            if str1[i] not in table:
                table[str1[i]] = 1
            elif str1[i] in table:
                table[str1[i]] += 1

        for i in range(0, len(str2)):
            if str2[i] in table:
                if table[str2[i]] == 1:
                    del table[str2[i]]
                else:
                    table[str2[i]] -= 1

        if len(table.keys()) == 0:
            return True
        return False