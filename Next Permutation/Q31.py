class Solution(object):
    def nextPermutation(self, nums):
            x=-1
            for i in range (len(nums)-2,-1,-1):
                if(nums[i]<nums[i+1]):
                        x=i
                        break
            b=-1
            if(x != -1):
                for i in range (len(nums)-1,x,-1):
                    if(nums[i]>nums[x]):
                
                        b=i
                        break
                self.swap(x,b,nums)
            self.reverse(x+1,nums)
            print(nums)
    
    def swap(self,x,b,nums):
        temp=nums[x]
        nums[x]=nums[b]
        nums[b]= temp
    
    def reverse(self,x,nums):
        s=x
        e=len(nums)-1
        while s<e:
            temp=nums[s]
            nums[s]=nums[e]
            nums[e]=temp
            s+=1
            e-=1
        
