import random


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

    def more(self, other_card): #возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра
        # При равенстве значений, сравниваем масти
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) > suits.index(other_card.suit)
        else:
            return values.index(self.value) > values.index(other_card.value)

    def less(self, other_card): #проверяет является ли карта младше, чем карта в параметре
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) < suits.index(other_card.suit)
        else:
            return values.index(self.value) < values.index(other_card.value)


class Deck:

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # Список значений карт
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']  # Список мастей карт
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = ', '.join([card.to_str() for card in self.cards])
        return f"cards[{len(self.cards)}] {cards_str}"

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        return random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")

