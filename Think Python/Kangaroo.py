class Kangaroo:


    def __init__(self, name, contents=None):
        """ pouch_contents should be a list"""
        self.name = name
        if contents == None:
            contents = []
        self.contents = contents

    def put_in_pouch(self, obj):
        self.contents.append(obj)

    def __str__(self):
        s = self.name + ' has pouch contents:'
        for obj in self.contents:
            s = s + '     ' + object.__str__(obj)
        return s

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
