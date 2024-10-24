import timeit

# ЖАДІБНИЙ АЛГОРИТМ
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin  # Скільки монет даного номіналу можемо взяти
        if count > 0:
            result[coin] = count
            amount -= coin * count  # Віднімаємо вартість цих монет із загальної суми
    return result


print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
# print(find_coins_greedy(11300000))  # {50: 226000}

greedy_time = timeit.timeit('find_coins_greedy(113)', globals=globals(), number=1000)
print("Час виконання жадібного алгоритму  на 1000 прогонів:", greedy_time, "секунд")