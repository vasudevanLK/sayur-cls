nums=[1,2,3,4,5]
min_num=nums[0]
max_num=nums[0]
for i in range(0,len(nums)):
    if(nums[i] > min_num):
        max_num=nums[i]
    else:
        min_val=nums[i]
        

print(min_val)    