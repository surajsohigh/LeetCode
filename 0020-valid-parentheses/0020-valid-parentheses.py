class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        mapping = { '(': ')', '{': '}', '[': ']' }
        for i in s:
            if li and i == mapping.get(li[-1]):
                li.pop()
            else:
                li.append(i)
                
        print(li)
        return not li
            
            
            
# class Solution:
#     def isValid(self, s: str) -> bool:
#         li = []
#         mapping = {'(': ')', '{': '}', '[': ']'}
#         for i in s:
#             if li and mapping.get(li[-1]) == i:
                
#                 li.pop()
#             else:
#                 li.append(i)
#         return not li