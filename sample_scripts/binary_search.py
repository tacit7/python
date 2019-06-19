import math

def search1(lst: List, target: Int, left: Int, rigth: Int):
    if left > right: # this doesn't make sense so...
        return false # <-- return false

    if lst[middle_point(left, right)]:
        return true
    elif target < middle_point(left, right):
        return search1(lst, left, right)
    else:
        shrinked_stack = middle_point(left, middle_point(left, right))
        return search1(lst, target, shrinked_stack, right)

    def middle_point(left, right):
        return math.floor((left + right) / 2)



