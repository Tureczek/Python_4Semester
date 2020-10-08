class Deck:

    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, x):
        return self.cards[x]

    def length(self):
        return len(self.cards)

    def __add__(self, other):
        de = Deck()
        de.cards = self.cards + other.cards
        return de

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f'Cards: {self.cards}'

    def __delitem__(self, x):
        del(self.cards[x])

    def __setitem__(self, key, value):
        self.cards[key] = value


d = Deck()
d1 = Deck()


print(len(d))
print(d.__add__(d + d1))
print(d.__repr__())
print(d.__str__())
d.__delitem__(0)
d.__setitem__(1, 1000)
print(d.__str__())
