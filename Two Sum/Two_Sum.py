class Solution(object):
    def twoSum(self, nums, target):
        final=[]
        for i in range(len(nums)):
            check=False
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        final.append(i)
                        final.append(j)
                        check=True
                        break
            if check==True:
                break
        return final