#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/8/24:10:00
# @email: 13259727865@163.com
from typing import List


class Solution(object):
    def twoSum(self,nums:List[int],target:int):
        s = 0
        for i in nums:
            j = target - i
            try:
                 j_index= nums.index(j,s+1)
            except:
                print("未找到")
                s += 1
            else:
                return s,j_index

if __name__ == '__main__':
    a = Solution()
    nums = [3,2,4,2,1,4,2,3,4,5,6,5,4,3,6]
    target = 8
    print(a.twoSum(nums, target))

