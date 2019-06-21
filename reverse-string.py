class Solution:
    def reverse(self, x):
        if x > 2147483647 or x < -2147483647:
            return 0
        if x > 0:
          return self.reverse_positive(x)
        if x < 0:
          return (self.reverse_positive(x * -1) * -1)
        else:
          return 0

    def reverse_positive(self, x):
        reverse = 0
        while x != 0:
            tail = x % 10
            x = x / 10
            reverse = reverse + tail

            if x == 0:
                return reverse

            reverse = reverse * 10

