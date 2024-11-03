import turtle


def draw_branch(branch_length, level):
    if level == 0:
        return

    # Малюємо гілку
    turtle.forward(branch_length)

    # Малюємо праву гілку
    turtle.right(20)
    draw_branch(branch_length * 0.7, level - 1)

    # Малюємо ліву гілку
    turtle.left(40)
    draw_branch(branch_length * 0.7, level - 1)

    # Повертаємось до попередньої позиції
    turtle.right(20)
    turtle.backward(branch_length)


def draw_pythagorean_tree(level):
    # Налаштування початкових параметрів
    turtle.left(90)  # Повертаємо вгору
    turtle.up()      # Піднімаємо перо
    turtle.backward(100)  # Зсув назад для початку
    turtle.down()    # Опускаємо перо
    turtle.color("green")
    turtle.pensize(2)

    # Малюємо дерево
    draw_branch(100, level)


def main():
    # Запитуємо рівень рекурсії у користувача
    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))

    # Налаштування вікна
    turtle.speed(0)  # Максимальна швидкість
    turtle.title("Дерево Піфагора")

    # Малюємо дерево
    draw_pythagorean_tree(level)

    # Завершення
    turtle.done()


if __name__ == "__main__":
    main()
