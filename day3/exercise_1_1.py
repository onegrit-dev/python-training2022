from card import ShuffledCards

shuffled_cards = ShuffledCards()
cards = []
for _ in range(5):
    card = shuffled_cards.draw()
    cards.append(card)

print(cards)

"""
【備考】

import card

shuffled_cards = card.ShuffledCards()

としてもよい。
"""

"""
【実行結果】（例）

['♠2', '♡K', '♡3', '♠K', '♡2']
"""
