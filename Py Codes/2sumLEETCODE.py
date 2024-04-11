# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#-----------------------------------------------------------------------------------------
def twosum():
  
 nums=[]
 n = int(input("Enter no. of elements :"))

 for i in range(0,n):
   ele=int(input("Enter your elements : "))
    
   nums.append(ele)
  
   print(nums)

 target= int(input("Enter your target : "))
  #need smth to start adding every index with every index combination possible, then
  #take those values and present if them in a list if the sum is equal to target

 prevhashmap={}

 for i,n in enumerate(nums):
    diff=target-n
    if diff in prevhashmap:
      indices= [prevhashmap[diff],i]
      print(indices)  
    prevhashmap[n]=i
     

twosum()

#WEAK POINTS:
  #LEARN HASHMAPS
  #LEARN LOOPS PROPERLY
  #LEARN INBUILT FUNCTIONS LIKE ENUMERATE
  

  
  
  