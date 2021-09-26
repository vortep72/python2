class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            "Spades": "\u2660",
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']     # Список значений карт
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']       # Список мастей карт
cards = []
for value in values:
    for suit in suits:
        cards.append(Card(value, suit))

print(", ".join([card.to_str() for card in cards]))
cards_str = ', '.join([card.to_str() for card in cards])
print(f"cards[{len(cards)}] {cards_str}")
