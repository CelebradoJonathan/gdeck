class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self.count = 0

    def __getitem__(self, position):
        return self.cards[position]

    def __len__(self):
        return len(self.cards)

    def __next__(self):
        if self.count >= len(self.cards):
            raise StopIteration
        current = self.cards[self.count]
        self.count += 1
        return current

    def __repr__(self):
        some_str = ""
        for card in self.cards:
            some_str += "\t{}\n".format(card)
        return some_str





