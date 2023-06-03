#!/usr/bin/env python
# coding: utf-8

# In[ ]:

Qustion 1



# In[ ]:
import sys
def tsum_closet(nums,x,n):
    closetsum=sys.maxsize
    nums.sort()
    for i in range(n-2):
        pt1=i+1
        pt2=n-1
        while(pt1<pt2):
                sum=nums[i]+nums[pt1]+nums[pt2]
                if (abs(x-sum)<abs(x-closetsum)):
                    closetsum=sum
                if sum>x:
                    pt2-=1
                else:
                    pt1+=1
                print(closetsum)    
    return(closetsum)




# In[ ]:

Question 4



# In[ ]:
def bisearch(nums,target):
    start=0
    end=len(nums)-1
    while(start<=end):
        mid=(start+end)//2
        
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return end+1
        




# In[ ]:

Question 5



# In[ ]:
def plusone(digits):
  index=len(digits)-1
  while index>=0 and digits[index]==9:
    digits[index]= 0
    index-=1
  
  if index<0:
    digits.insert(0,1)
  else:
    digits[index]+=1
  return(digits)




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




