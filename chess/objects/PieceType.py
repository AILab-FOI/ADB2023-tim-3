from persistent import Persistent

class PieceType(Persistent):
    def __init__(self, typeid, typename):
        self.typeid = typeid
        self.typename = typename
        
