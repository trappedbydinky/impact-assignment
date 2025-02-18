
class Solution:
    def largestNumber(self, nums):

        nums_str = list(map(str, nums))

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        nums_str.sort(key=cmp_to_key(compare))

        result = ''.join(nums_str)

        if result[0] == '0':
            return '0'
        else:
            return result
