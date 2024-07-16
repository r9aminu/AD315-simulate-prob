import random
import matplotlib.pyplot as plt

def draw_card(total_cards):
    images = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = []
    for image in images:
        for rank in ranks:
            deck.append((rank, image))

    draws = []
    for _ in range(total_cards):
        card = random.choice(deck)
        draws.append(card)

    red_cards = ['hearts', 'diamonds']
    num_red_cards = 0
    num_black_cards = 0
    for card in draws:
        rank, image = card
        if image in red_cards:
            num_red_cards += 1
        else:
            num_black_cards += 1

    return num_red_cards, num_black_cards

total_cards = 20

num_red_cards, num_black_cards = draw_card(total_cards)

print("Num red: ", num_red_cards)
print("Num black: ", num_black_cards)

labels = ['Red Cards', 'Black Cards']
counts = [num_red_cards, num_black_cards]

plt.bar(labels, counts, color=['red', 'black'])
plt.xlabel('Card Color')
plt.ylabel('Count')
plt.title('Count of Red versus Black Cards')
plt.show()
