class CEdge:
    def __init__(self, src=None, dest=None, w=None, info="white") -> None:
        self.src = src
        self.dest = dest
        self.w = w
        self.info = info
