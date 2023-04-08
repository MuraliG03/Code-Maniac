class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def addTwoLists(first, second):
    head = None
    prev = None
    temp = None
    carry = 0
    while first is not None or second is not None:
        if first is None:
            firstData = 0
        else:
            firstData = first.data
        if second is None:
            secondData = 0
        else:
            secondData = second.data
        Sum = carry + firstData + secondData
        if Sum >= 10:
            carry = 1
        else:
            carry = 0
        Sum %= 10
        temp = Node(Sum)
        if head is None:
            head = temp
        else:
            prev.next = temp
        prev = temp
        if first is not None:
            first = first.next
        if second is not None:
            second = second.next
    if carry > 0:
        temp.next = Node(carry)
    return head



n1 = Node(2)
n2 = Node(3)
n3 = Node(1)
n1.next = n2
n2.next = n3

m1 = Node(5)
m2 = Node(2)
m3 = Node(1)
m1.next = m2
m2.next = m3

result = addTwoLists(n1, m1)
while result is not None:
    print(result.data, end=" ")
    result = result.next
