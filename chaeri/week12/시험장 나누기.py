class Node:
    def __init__(self,num):
        self.data=num
        self.left=self.right=None


class Binary_tree:
    def __init__(self):
        self.root=None

    def Node_insert(self,num):
        if self.root==None:
            self.root=Node(num)
        else:
            self.curr=self.root
            while True:
                if num<self.curr.data:
                    if self.curr.left==None:
                        self.curr.left=Node(num)
                        break
                    else:
                        self.curr=self.curr.left
                else:
                    if self.curr.right==None:
                        self.curr.right=Node(num)
                        break
                    else:
                        self.curr=self.curr.right
                        