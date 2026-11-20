class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if len(A)>len(B):
            A, B = B, A

        m = len(A)
        n = len(B)

        total = m + n
        left_size = (total +1)//2

        left = 0
        right = m

        while left <=right:
            i = (left + right)//2

            j = left_size -i

            Aleft = A[i-1] if i>0 else float("-inf")
            Aright = A[i] if i<m else float("inf")

            Bleft = B[j-1] if j>0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return float(max(Aleft, Bleft))

                return (
                    max(Aleft, Bleft)
                    + min(Aright, Bright)
                ) / 2

            # Too many elements from A on the left
            elif Aleft > Bright:
                right = i - 1

            # Too few elements from A on the left
            else:
                left = i + 1

       


