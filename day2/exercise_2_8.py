cards = [
    '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
    '◇A', '◇2', '◇3', '◇4', '◇5', '◇6', '◇7', '◇8', '◇9', '◇10', '◇J', '◇Q', '◇K',
    '♡A', '♡2', '♡3', '♡4', '♡5', '♡6', '♡7', '♡8', '♡9', '♡10', '♡J', '♡Q', '♡K',
    '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
]

for card in cards:
    print(card)

"""
【備考】
逆から表示するためのコードはこちら。
listのreverse()メソッドを使うと、元のlistオブジェクトは書き換えられるが戻り値がNoneになるため、TypeErrorが発生する。
そこで、組み込み関数のreversed()を使う。

for card in reversed(cards):
    print(card)
"""

"""
【実行結果】（例）

♠A
♠2
♠3
♠4
♠5
♠6
♠7
♠8
♠9
♠10
♠J
♠Q
♠K
◇A
◇2
◇3
◇4
◇5
◇6
◇7
◇8
◇9
◇10
◇J
◇Q
◇K
♡A
♡2
♡3
♡4
♡5
♡6
♡7
♡8
♡9
♡10
♡J
♡Q
♡K
♣A
♣2
♣3
♣4
♣5
♣6
♣7
♣8
♣9
♣10
♣J
♣Q
♣K
"""
