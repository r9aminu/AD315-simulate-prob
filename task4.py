import random
import matplotlib.pyplot as plt

both_heads = 0
at_least_one_head = 0

for _ in range(50):
    first_flip = random.choice(["H", "T"])
    second_flip = random.choice(["H", "T"])

    if first_flip == "H" and second_flip == "H":
        both_heads += 1

    if first_flip == "H" or second_flip == "H":
        at_least_one_head += 1

print("Both heads:", both_heads)
print("At least one head:", at_least_one_head)

plt.bar(["Both heads", "At least one head"], [both_heads, at_least_one_head])
plt.ylabel('Occurrences')
plt.title('Coin Flip')
plt.show()
