import random
import matplotlib.pyplot as plt


def simulate_dice_throws(num_throws):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

    probabilities = {sum_: count / num_throws for sum_,
                     count in sums_count.items()}
    return probabilities


num_throws = 100000
probabilities = simulate_dice_throws(num_throws)

analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

print("Сума\tЙмовірність (Монте-Карло)\tЙмовірність (Аналітична)")
for sum_, mc_prob in probabilities.items():
    print(f"{sum_}\t{mc_prob:.4f}\t\t\t{analytical_probabilities[sum_]:.4f}")

sums = list(probabilities.keys())
mc_probs = list(probabilities.values())
analytic_probs = list(analytical_probabilities.values())

plt.figure(figsize=(10, 6))
plt.plot(sums, mc_probs, marker='o', label='Монте-Карло')
plt.plot(sums, analytic_probs, marker='x', linestyle='--',
         color='orange', label='Аналітичні')
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум чисел на двох кубиках (Монте-Карло vs Аналітичні)')
plt.legend()
plt.grid()
plt.show()
