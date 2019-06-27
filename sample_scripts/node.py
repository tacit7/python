class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.nextval = None

    def to_s(self):
        return f'{self.data} => {self.pnextval()}'

    def pnextval(self):
        if self.nextval is None:
            return 'None'
        else:
            return self.nextval.to_s()

# class RanNode(object):
#     def __init__(self, value=None, next=None, random=None):
#         self.value = value
#         self.next = next
#         self.random = random
# from node import Node
