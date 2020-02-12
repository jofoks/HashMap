class Planar_Map():
    def __init__(self, size:int, data=None, DBPath=None):
        self.size = size
        self.map = [None] * self.size
        self.data = data
        if self.data is not None:
            for obj in data:
                self.add(obj)

    def __repr__(self):
        return f'Planar_Map: \nDistribution: {self.getLenghts()}'
    
    def get_hash(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash%self.size

    def add(self, obj):
        ''' Adds the value in the map in the corresponding position'''
        key = obj.getKey()
        loc = self.get_hash(key)
        tup = (key, obj)

        if self.map[loc] is None:
            self.map[loc] = [tup]
            return True
        else:
            keys = [i[0] for i in self.map[loc]]
            if key in keys:
                raise ValueError('Duplicate Value Found')
            self.map[loc].append(tup)
            return True
        
    def get(self, key):
        Loc = self.get_hash(key)
        if self.map[Loc] is None:
            return None
        for row in self.map[Loc]:
            if row[0] == key:
                return row

    def delete(self, key):
        Loc = self.get_hash(key)
        if self.map[Loc] is None:
                return False
        for n in range(len(self.map[Loc])):
            if self.map[Loc][n][0] == key:
                self.map[Loc].pop(n)
                return True
        return False
    
    def getSize(self):
        return self.size
    
    def getMap(self):
        return self.map

    def getStreet(self, row):
        return row['info']['address']['streetAddress']

    def getLenghts(self):
        dct = {}
        for index, i in enumerate(self.getMap()):
            if i == None:
                dct[f'pos: {index}'] = 0
            else:
                dct[f'pos: {index}'] = len(i)
        return dct
