class Note:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkStack:
    def __init__(self):
        self.head = Note(None)

    def add(self,item):
        p = Note(item)
        p.next = self.head.next
        self.head.next = p

    def len(self):
        p = self.head.next
        i = 0
        while p:
            i+=1
            # print(p.val)
            p = p.next
        return i

    def show(self):
        p = self.head.next
        while p.val:
            print("val",p.val)
            p = p.next

    def pop(self):
        res = self.head.next
        self.head.next = res.next
        return res.val

ls = LinkStack()
for i in range(4):
    ls.add(i)

print(ls.len())
ls.show()

l = ls.len()
sum = 0
for i in range(l):
    num = ls.pop()
    l-=1
    sum = sum+num*10**l

print(sum)