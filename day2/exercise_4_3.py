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


"""
「♣」が出る前に「A」を出したら勝ちというゲーム（「♣A」は勝ちとする）
"""
shuffled_cards = ShuffledCards()
count = 0
while not shuffled_cards.is_empty():
    count += 1
    card = shuffled_cards.draw()
    print('{}枚目: {}'.format(count, card))
    if card[1:] == 'A':
        print('勝ち')
        break
    if card[0] == '♣':
        print('負け')
        break

"""
【実行結果】（例）

1枚目: ♠Q
2枚目: ♠10
3枚目: ♡J
4枚目: ♡K
5枚目: ♣A
勝ち
"""
