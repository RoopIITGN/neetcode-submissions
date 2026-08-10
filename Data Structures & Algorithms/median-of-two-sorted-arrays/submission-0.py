class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B)<len(A):
            A, B = B, A 
        total = len(A)+len(B)
        half = (total+1)//2
        l, r = 0, len(A)

        while(l <= r):
            i = (l+r)//2
            j = half-i
            A_l = A[i-1] if i>0 else float('-inf')
            A_r = A[i] if i<len(A) else float('inf')
            B_l = B[j-1] if j>0 else float('-inf')
            B_r = B[j] if j<len(B) else float('inf')
            
            if(A_l<=B_r) and (B_l<A_r):
                if(total%2 != 0):
                    return float(max(A_l, B_l))
                else:
                    return float((max(A_l, B_l) + min(A_r, B_r))/2)
            if(A_l > B_r):
                r = i-1
            else:
                l = i+1