def targetSum(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R = R - 1 # or R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]
        
arr = list(map(int, input("enter array elements separated by spaces: ").split()))
target = int(input("enter your target value"))
print(targetSum(arr, target))
