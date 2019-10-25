from gdeck import gdeck
import pytest


def test_card():
    card_obj = gdeck.Card("Wizard", "Oz")
    assert str(card_obj) == "Wizard of Oz"


def test_card_instance():
    card_obj = gdeck.Card("Wizard", "Oz")
    assert isinstance(card_obj, gdeck.Card)


def test_deck():
    deck_str = "[Ace of Diamonds, Ace of Hearts, Ace of Clubs, Ace of Spades," \
               " 2 of Diamonds, 2 of Hearts, 2 of Clubs, 2 of Spades," \
               " 3 of Diamonds, 3 of Hearts, 3 of Clubs, 3 of Spades," \
               " 4 of Diamonds, 4 of Hearts, 4 of Clubs, 4 of Spades," \
               " 5 of Diamonds, 5 of Hearts, 5 of Clubs, 5 of Spades," \
               " 6 of Diamonds, 6 of Hearts, 6 of Clubs, 6 of Spades," \
               " 7 of Diamonds, 7 of Hearts, 7 of Clubs, 7 of Spades," \
               " 8 of Diamonds, 8 of Hearts, 8 of Clubs, 8 of Spades," \
               " 9 of Diamonds, 9 of Hearts, 9 of Clubs, 9 of Spades," \
               " 10 of Diamonds, 10 of Hearts, 10 of Clubs, 10 of Spades," \
               " Jack of Diamonds, Jack of Hearts, Jack of Clubs, Jack of Spades," \
               " Queen of Diamonds, Queen of Hearts, Queen of Clubs, Queen of Spades," \
               " King of Diamonds, King of Hearts, King of Clubs, King of Spades]"
    deck = gdeck.Deck()
    assert deck_str == str(deck)


def test_deck_instance():
    deck_obj = gdeck.Deck()
    assert isinstance(deck_obj, gdeck.Deck)


def test_deck_iter():
    deck_obj = gdeck.Deck()
    assert isinstance(iter(deck_obj), gdeck.Deck)


def test_deck_len():
    deck_obj = gdeck.Deck()
    assert len(deck_obj) == 52


def test_deck_getitem():
    deck_obj = gdeck.Deck()
    assert str(deck_obj[0:9]) == "[Ace of Diamonds, Ace of Hearts, Ace of Clubs, Ace of Spades," \
                                 " 2 of Diamonds, 2 of Hearts, 2 of Clubs, 2 of Spades, 3 of Diamonds]"


def test_deck_next():
    with pytest.raises(StopIteration):
        deck_obj = gdeck.Deck()
        for deck in iter(deck_obj):
            next(deck_obj)
        next(deck_obj)
