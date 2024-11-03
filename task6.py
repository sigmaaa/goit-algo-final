def greedy_algorithm(items, budget):
    items_list = [(name, item['cost'], item['calories'])
                  for name, item in items.items()]

    # Сортуємо елементи за співвідношенням калорій до вартості в спадаючому порядку
    items_list.sort(key=lambda x: x[2] / x[1], reverse=True)

    total_calories = 0
    selected_items = {}

    for name, cost, calories in items_list:
        while budget >= cost:
            budget -= cost
            total_calories += calories
            selected_items[name] = selected_items.get(name, 0) + 1

    return total_calories, selected_items


def dynamic_programming_algorithm(items, budget):
    dp = [0] * (budget + 1)
    item_names = list(items.keys())

    for name in item_names:
        cost = items[name]['cost']
        calories = items[name]['calories']

        for j in range(cost, budget + 1):
            dp[j] = max(dp[j], dp[j - cost] + calories)

    total_calories = dp[budget]
    selected_items = {}
    remaining_budget = budget

    for name in reversed(item_names):
        cost = items[name]['cost']
        calories = items[name]['calories']

        while remaining_budget >= cost and dp[remaining_budget] == dp[remaining_budget - cost] + calories:
            selected_items[name] = selected_items.get(name, 0) + 1
            remaining_budget -= cost

    return total_calories, selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Визначаємо бюджет
budget = 250

# Виклик жадібного алгоритму
greedy_result = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: Загальна калорійність = {
      greedy_result[0]}, Вибрані страви = {greedy_result[1]}")
dp_result = dynamic_programming_algorithm(items, budget)
print(f"Алгоритм динамічного програмування: Загальна калорійність = {
      dp_result[0]}, Вибрані страви = {dp_result[1]}")
