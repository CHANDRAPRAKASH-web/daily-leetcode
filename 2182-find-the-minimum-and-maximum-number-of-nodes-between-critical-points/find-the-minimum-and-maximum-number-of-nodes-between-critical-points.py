
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        count=[]
        for i in range(1,len(nums)-1):
            if (nums[i]<nums[i-1] and nums[i]<nums[i+1]) or (nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                count.append(i)
        if len(count)<2:
            return [-1,-1]
        max_index=count[-1]-count[0]
        min_index=float('inf')
        for i in range(1,len(count)):
            min_index=min(min_index,count[i]-count[i-1])
        return [min_index,max_index]

        