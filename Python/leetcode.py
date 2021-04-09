'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. '''


def target_nums(nums,target):
    for i in range(len(nums)-1):
        for v in range(len(nums)-1):
            if nums[i] + nums[v+1] == target:
                print(f'{nums[i]} + {nums[v+1]} = your target of {target}')

        # else:
        #
        #     continue


nums = [6, 4, 5, 15,2,7]
target_nums(nums,9)
