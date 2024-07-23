def swapNum(nums, i):
    if i >= len(nums)/2:
        return nums
    else:
        nums[i], nums[len(nums) - i -1] =  nums[len(nums) - i -1], nums[i]
        i +=1
        return swapNum(nums, i)
       



if __name__ == '__main__':
    listdetails = ["apple", "banana", "cherry","pine apple","Water Melon"]
    print(swapNum(listdetails, 0))
   
    