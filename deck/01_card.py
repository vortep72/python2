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


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Hearts")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")