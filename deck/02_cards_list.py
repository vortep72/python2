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

spades_cards = []
for value in values:
    spades_cards.append(Card(value, 'Spades'))
    print(", ".join([card.to_str() for card in spades_cards]))

hearts_cards = []
for value in values:
    hearts_cards.append(Card(value, 'Hearts'))
    print(", ".join([card.to_str() for card in hearts_cards]))

diamonds_cards = []
for value in values:
    diamonds_cards.append(Card(value, 'Diamonds'))
    print(", ".join([card.to_str() for card in diamonds_cards]))


clubs_cards = []
for value in values:
    clubs_cards.append(Card(value, 'Clubs'))
    print(", ".join([card.to_str() for card in clubs_cards]))


