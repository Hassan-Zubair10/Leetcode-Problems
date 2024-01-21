class Solution:
    def isHappy(self, n: int) -> bool:
        def step(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                number = number // 10
                total_sum += digit ** 2
            return total_sum

        slow = n
        fast = step(n)
    
        while slow != fast:
            slow = step(slow)
            fast = step(step(fast))
    
        if fast == 1:
            return True
        return False

