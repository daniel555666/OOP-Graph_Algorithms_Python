class CNode:

    def __init__(self, pos=None, id=None, info="white", previous=None, length=None, rank=0):
        self.pos = pos
        self.id = id
        self.info = info
        self.previous = previous
        self.length = length
        self.rank = rank
