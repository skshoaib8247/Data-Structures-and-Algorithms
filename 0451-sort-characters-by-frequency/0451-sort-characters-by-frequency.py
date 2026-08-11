class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for j in s:
            count[j] = count.get(j, 0) + 1

        res = ""

        for i in range(len(s), 0, -1):
            for j in count:
                if count[j] == i:
                    res += j * i

        return res
# class Solution:
#     def frequencySort(self, s: str) -> str:
        


# class Solution:
#     def frequencySort(self, s: str) -> str:
#         if s==" ":
#           return ""
#         res=""
#         done=""
#         for i in range(len(s),0,-1):
#             for j in range(len(s)):
#                 if s.count(s[j])==i and s[j] not in done:
#                     res+=s[j]*i
#                     done+=s[j]
#         return res     
# FAILS AT THIS
# "loveleetcode"
# "eeeelolovtcd"
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         if s == " ":
#             return ""

#         res = ""
#         done = ""

#         for i in range(len(s), 0, -1):
#             for j in range(len(s)):
#                 if s[j] not in done and s.count(s[j]) == i:
#                     res += s[j] * i
#                     done += s[j]

#         return res