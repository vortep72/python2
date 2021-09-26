import random


class Card:

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        symbols = {
            "Spades": "\u2660",
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card): #возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра
        # При равенстве значений, сравниваем масти
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) > suits.index(other_card.suit)
        else:
            return values.index(self.value) > values.index(other_card.value)

    def __ls__(self, other_card): #проверяет является ли карта младше, чем карта в параметре
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
        self.next_card_index = 0
        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

    def __str__(self):
        cards_str = ", ".join([str(card) for card in self.cards])
        return f'deck[{len(self.cards)}]{cards_str}'

    def __iter__(self):
        return self

    def __next__(self):
        card = self.cards[self.next_card_index]
        self.next_card_index += 1
        if self.next_card_index >= len(self.cards):
            raise StopIteration
        return card

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        return random.shuffle(self.cards)


deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")
    if card1 < card2:
        print(f"{card1} больше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html