

def quickSort(nums):
    

    less = []
    equal = []
    greater = []

    if len(nums) > 1:
        pivot = nums[0]
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
        
        return quickSort(less)+equal+quickSort(greater)
    else: 
        return nums

nums= [0,0,0,0,0,0,0,0]
j=0
for j in range(8):
 nums[j] = input('inserta numero: ')

num= quickSort(nums)
print(*num)