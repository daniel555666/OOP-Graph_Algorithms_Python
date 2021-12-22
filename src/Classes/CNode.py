class CNode:

    def __init__(self, pos: tuple = None, id: int = None, info: str = "white", previous=None, length=None,
                 rank: int = 0):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.id = id
        self.info = info
        self.previous = previous
        self.length = length
        self.rank = rank

    def __str__(self) -> str:
        return f"""( CNode id= {self.id} , info= {self.info} , previous= {self.previous} , length= {self.length},
         rank=' {self.rank} , pos= {self.x} , {self.y}, {self.z} ) \n"""

    def __repr__(self) -> str:
        return f""" ( CNode id= {self.id} , info= {self.info} , previous= {self.previous} , length= {self.length},
         rank=' {self.rank} , pos= {self.x} , {self.y}, {self.z} ) \n"""
