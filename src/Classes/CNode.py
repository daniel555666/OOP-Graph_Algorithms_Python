class CNode:

    def __init__(self, pos:tuple =None, id :int =None, info :str ="white", previous =None, length=None, rank :int =0):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.id = id
        self.info = info
        self.previous = previous
        self.length = length
        self.rank = rank

    def __lt__(self, other):
        return self.length<other.length