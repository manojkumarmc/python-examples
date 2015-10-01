class MultiLevelDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value



d = MultiLevelDict()

d['a']['b'] = 'Try this'

print d
