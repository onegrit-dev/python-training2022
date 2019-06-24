from day3 import cards

shuffled_cards = cards.ShuffledCards()
for i in range(100):
    try:
        card = shuffled_cards.draw()
        print('{}枚目={}'.format(i + 1, card))
    except cards.EndOfCardException as ex:
        print(ex)
        break
