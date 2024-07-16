import random
import matplotlib.pyplot as plt

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range(60):
    side = random.randint(1, 6)
    if side == 1:
        one += 1
    elif side == 2:
        two += 1
    elif side == 3:
        three += 1
    elif side == 4:
        four += 1
    elif side == 5:
        five += 1
    elif side == 6:
        six += 1

print(one, two, three, four, five, six)

# Plot
counts = [one, two, three, four, five, six]
sides = ['1', '2', '3', '4', '5', '6']

plt.bar(sides, counts)
plt.xlabel('Dice Number')
plt.ylabel('Count')
plt.title('Rolling Dice')
plt.show()
