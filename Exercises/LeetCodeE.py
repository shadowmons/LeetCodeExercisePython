'''
Created on Jan 29, 2024

@author: victo
'''

class LeetCodeE:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    #You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    #Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    #The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    
    @staticmethod   
    def MergeSortedArray1(nums1, nums2, m, n):
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
        
    @staticmethod  
    def MergeSortedArray2( nums1, nums2, m, n):
        i = m-1
        j = n-1
        k = m + n -1
        while j >= 0:
            if i >= 0 and nums1[i]>nums2[j]:
                nums1[k]= nums1[i]
                i-=1
            else:
                nums1[k]= nums2[j]
                j-=1
            k-=1
            
    #Array1 = [1,2,3,4,7,0,0,0]
    #Array2 = [2,5,6]
    #LeetCodeE().MergeSortedArray1(Array1 , Array2 , 5, 3)
    
    #Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    @staticmethod  
    def removeElement1( nums, val):
        j=0
        
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[j] = nums[i]
                j+=1
        return j
    
    #Array1 = [1,2,2,3,5,7,2]
    #print(LeetCodeE().removeElement1(Array1, 2))
    #print(Array1)
    
    #Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    #Consider the number of unique elements of nums to be k
    @staticmethod  
    def removeDuplicatesSort1 (nums):
        j =1
        aux = nums[0]
        for i in range(len(nums)-1):
            if (nums[i+1]!= aux):
                aux = nums[i+1]
                nums[j] =nums[i+1]
                j+=1
        return j
    
    #Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
    #Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
    #Return k after placing the final result in the first k slots of nums.
    #Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    @staticmethod
    def removeDuplicatesSortTwice2 (nums):
        j=1
        cont = 0
        for i in range (1,len(nums)):
            if(nums[i]==nums[i-1]):
                cont+=1
            else:
                cont = 0
                
            if (cont < 2):
                nums[j]= nums[i]
                j+=1
                
        return j
    
    #Array1 = [0,0,1,1,1,2,2,2,3,3,4]
    #print(LeetCodeE().removeDuplicatesSortTwice2(Array1))
    #print(Array1)
    
    #Given an array nums of size n, return the majority element.
    #The majority element is the element that appears more than n/2 times. You may assume that the majority element always exists in the array.
    
    @staticmethod
    def MajorityElement (nums):
        cont = 1
        aux = nums[0]
        for i in range(1,len(nums)):
            if (nums[i]==aux):
                cont+=1
            else:
                cont-=1
                
            if(cont==0):
                aux=nums[i]
                cont=1
                
        return aux
    
    #Array1 = [2,0,0,1,1,1,2,2,3,3,4,2,2,2,2,2]
    #print(LeetCodeE().MajorityElement(Array1))
    #print(Array1)
    

    #Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    @staticmethod
    def RotateArray1(nums, k):
        k = k%len(nums)
        aux = 0
        arrayB = nums.copy()
        for i in range(len(nums)):
            if(i+k<len(nums)):
                aux = i+k
            else:
                aux = i+k-len(nums)
            nums[aux]=arrayB[i] 
    
    @staticmethod
    def RotateArray2(nums, k):
        k = k%len(nums)
        nums [:]= nums[-k:] + nums[:-k]
        
    #Array1 = [1,2,3,4,5,6,7,8,9]
    #LeetCodeE().RotateArray1(Array1,3)
    #print(Array1)
    
    #You are given an array prices where prices[i] is the price of a given stock on the ith day.
    #You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    #Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    @staticmethod
    def BestTimetoBuyandSellStock(prices):
        minValue = prices[0]
        diff = 0
        for i in range(1,len(prices)):
            if (prices[i]<minValue):
                minValue = prices[i]
                
            if (prices[i]-minValue>0):
                diff =max(diff,prices[i]-minValue)
        return diff
   
    #You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    #On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    #Find and return the maximum profit you can achieve.
    @staticmethod
    def BestTimetoBuyandSellStock2(prices):
        diff = 0
        for i in range(1,len(prices)):
            if (prices[i]>prices[i-1]):
                diff = diff +prices[i]-prices[i-1]
        return diff
        
        
    # Array1 = [7,1,5,3,6,7,4,6,2]
    #print(LeetCodeE().BestTimetoBuyandSellStockw(Array1))
        
    @staticmethod
    def JumpGameNotUse (nums):
        Total= 0
        Jump = nums[0]
        AP = 0
        flag = False
        while (flag == False):
            if(Total>=len(nums)-1):
                flag = True
            else:
                aux= 0
                PP = 0
                PJ = 0
                PT = 0
                for i in range (AP ,AP + Jump):
                    if(aux<i+1-AP+nums[i+1]):
                        aux = i+1-AP+nums[i+1]
                        PT= i+1-AP
                        PP = i+1
                        PJ = nums[i+1]
                Total = Total + PT
                Jump = PJ
                AP = PP
                if (Jump ==0):
                    break
                
                    
        return flag


    #You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    #Return true if you can reach the last index, or false otherwise.
    @staticmethod
    def JumpGame(nums):
        jump = 0
        for i in nums:
            if jump < 0:
                return False
            elif i > jump:
                jump = i
                
            jump-=1
                
                    
        return True
  
  
    #You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    #Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    #0 <= j <= nums[i] and
    #i + j < n
    #Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
    
    
   
        
        
        
        
        
        
        
        
        
        