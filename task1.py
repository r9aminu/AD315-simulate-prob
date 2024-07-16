import random
import matplotlib.pyplot as plt

head_total = 0
tail_total = 0
count = 0

while count < 100:
    side = random.randint(1, 2)
    if side == 1:
        head_total += 1
    else:
        tail_total += 1
    count += 1

# Plot
labels = ['Heads', 'Tails']
totals = [head_total, tail_total]

plt.bar(labels, totals, color=['blue', 'orange'])
plt.xlabel('Coin Side')
plt.ylabel('Count')
plt.title('Heads vs Tails')
plt.show() 