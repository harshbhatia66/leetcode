class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Half the integer x -> a and check if the square of a is equal to x
        # If it is larger than x, keep halfing a
        # If it is smaller than x, choose the larger half
       
        if x < 2:
            return x
        
        left = 1
        right = x // 2
        mid = 0
        # Binary search 
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid > x:
                # Reduce search space
                right = mid - 1
            else:
                left = mid + 1
            
        return right
    

# Initiate class
calc = Solution()

print(calc.mySqrt(9))