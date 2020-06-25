from time import time

from day3.cards import ShuffledCards

t = time()

success_count = 0
total_count = 1000000

for _ in range(total_count):
    cards = ShuffledCards()
    hands = []
    # 5枚引く
    for _ in range(5):
        card = cards.draw()
        hands.append(card)

    # フラッシュの確率計算
    colors = [hand[:1] for hand in hands]
    print(colors)
    if len(set(colors)) == 1:
        print('フラッシュ成立！')
        success_count += 1

print('フラッシュの確率は {}回中 {}回（{:.2f}%）でした。'.format(
    total_count, success_count, (success_count / total_count) * 100))

print('Finished in {:.2f} sec.'.format(time() - t))
