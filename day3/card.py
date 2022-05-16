import random


class ShuffledCards:
    CARDS = [
        '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
        '◇A', '◇2', '◇3', '◇4', '◇5', '◇6', '◇7', '◇8', '◇9', '◇10', '◇J', '◇Q', '◇K',
        '♡A', '♡2', '♡3', '♡4', '♡5', '♡6', '♡7', '♡8', '♡9', '♡10', '♡J', '♡Q', '♡K',
        '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
    ]

    def __init__(self):
        self._shuffled_cards = self.CARDS[:]
        random.shuffle(self._shuffled_cards)

    def is_empty(self):
        return len(self._shuffled_cards) == 0

    def draw(self):
        if not self.is_empty():
            return self._shuffled_cards.pop()
        else:
            return None
