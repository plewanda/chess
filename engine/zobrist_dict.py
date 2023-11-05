from collections import OrderedDict


class ZobristDict(OrderedDict):
    def __init__(self, limit):
        self.limit = limit
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
        if len(self) > self.limit:
            self.popitem(last=False)