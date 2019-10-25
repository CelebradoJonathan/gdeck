class Card:
    def __init__(self, rank, suit):
        """
        param rank: preferably a card rank, but can be anything
        param suit: preferably a card suit, but can be anything
        """
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

    def __init__(self):
        """
        Initializes a list of cards.
        """
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.cards):
            raise StopIteration
        current = self.cards[self.count]
        self.count += 1
        return current

    def __repr__(self):
        return str(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __len__(self):
        return len(self.cards)





