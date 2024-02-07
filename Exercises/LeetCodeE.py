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
  
    
    
   
        
        
        
        
        
        
        
        
        
        