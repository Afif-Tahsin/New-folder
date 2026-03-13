class pair_Elements():
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = 1

value = int(input("Enter sum of which you want to make this search: "))
print("index1=%d, index2=%d " %pair_Elements().twoSum((10, 20, 30, 40, 50, 60, 70),value))