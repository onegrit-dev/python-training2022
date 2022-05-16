from card import ShuffledCards

shuffled_cards = ShuffledCards()
cards = []
for _ in range(5):
    card = shuffled_cards.draw()
    cards.append(card)

print(cards)
