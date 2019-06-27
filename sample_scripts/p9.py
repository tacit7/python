class Solution(object):
    def __init__(self, x):
        self.number = x
        self.reverted_number = 0

    def isPalindrome(self):
        """
        :type x: int
        :rtype: bool
        """

        if self.number < 0 or self.multiple_of_ten():
            return False

        while(self.number > self.reverted_number):
            self.reverted_number = self.grow_reversed_number() + self.pop_from_number()
            self.shrink_number()
        self.remove_odd_number()
        return self.reverted_number == self.number


    def multiple_of_ten(self):
        if self.number % 10 is 0 and self.number is not 0 and self.number:
            return True
        else:
            return False

    def pop_from_number(self):
        pop = self.number % 10
        return pop

    def grow_reversed_number(self):
        self.reverted_number = self.reverted_number * 10
        return self.reverted_number

    def shrink_number(self):
        self.number = self.number // 10

    def remove_odd_number(self):
        if self.number < self.reverted_number:
            self.reverted_number = int(self.reverted_number /10)
