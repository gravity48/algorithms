from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        new=[]
        for i in range(len(nums)):
            new.append([nums[i],i])
        new=sorted(new,key=lambda x:x[0])
        new2d=[[new[0]]]
        for i in range(1,len(nums)):
            if new[i][0]-new[i-1][0]<=limit:
                new2d[-1].append(new[i])
            else:
                new2d.append([new[i]])
        for v in new2d:
            index=[]
            for m,n in v:
                index.append(n)
            index.sort()
            for i in range(len(index)):
                nums[index[i]]=v[i][0]
        return nums

class MySolution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        length = len(nums)
        new = [(num, index) for index, num in enumerate(nums)]
        new.sort(key=lambda x: x[0])
        pairs = [[new[0]]]
        for i in range(1, length):
            if new[i][0] - new[i-1][0] <= limit:
                pairs[-1].append(new[i])
            else:
                pairs.append([new[i]])
        for pair in pairs:
            index = [index for v, index in pair]
            index.sort()
            for i in range(len(index)):
                nums[index[i]] = pair[i][0]
        return nums

if __name__ == '__main__':
    MySolution().lexicographicallySmallestArray([1,5,3,9,8], 2)