class Node:
    def __init__(self,Mid):
        self.Mid=Mid
        self.left=None
        self.right=None
    def pushed(self,New_Mid):
        if Mid==None:
            return Node(New_Mid)
        else:
            if New_Mid>Mid:
                self.right=pushed(Mid.right,New_Mid)
            elif New_Mid<Mid:
                Mid.left=pushed(Mid.left,New_Mid)
            return Mid
        


Mid = None
Mid = pushed(Mid, 10)
Mid = add(Mid, 5)
Mid = add(Mid, 15)
