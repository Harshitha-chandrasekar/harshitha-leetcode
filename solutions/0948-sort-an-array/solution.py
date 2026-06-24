class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l,m,r):
            n1,n2 = arr[l:m+1],arr[m+1:r+1]
            l1 = len(n1)
            l2 = len(n2)
            ans = []
            i,j = 0,0
            while i<l1 and j<l2:
                if n1[i]<n2[j]:
                    ans.append(n1[i])
                    i = i+1
                else:
                    ans.append(n2[j])
                    j = j+1
                
            while i<l1:
                ans.append(n1[i])
                i = i+1
            while j<l2:
                ans.append(n2[j])
                j = j+1
            arr[l:r+1] = ans

        def mergesort(arr,l,r):
            if l == r:
                return arr
            
            m = (l+r)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr

        return mergesort(nums,0,len(nums)-1)
