
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums=[]
        #step-1: Convert linkded list into array
        while head:
            nums.append(head.val)
            head=head.next
        count=[]
        #step-2: Find the index of critical Points
        for i in range(1,len(nums)-1):
            if (nums[i]<nums[i-1] and nums[i]<nums[i+1]) or (nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                count.append(i)
        if len(count)<2:
            return [-1,-1]
        #step-3: Find the Max difference between index
        max_index=count[-1]-count[0]
        #step-4: Find the Min difference between index
        min_index=float('inf')
        for i in range(1,len(count)):
            min_index=min(min_index,count[i]-count[i-1])
        #step-5: Return the list of max and min difference
        return [min_index,max_index]

        