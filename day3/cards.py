import random


class EndOfCardException(Exception):
    pass


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

    def draw(self):
        if len(self._shuffled_cards) > 0:
            return self._shuffled_cards.pop()
        else:
            raise EndOfCardException('カードが無くなりました。')


if __name__ == '__main__':
    shuffled_cards = ShuffledCards()
    for i in range(100):
        try:
            card = shuffled_cards.draw()
            print('{}枚目={}'.format(i + 1, card))
        except EndOfCardException as ex:
            print(ex)
            break
