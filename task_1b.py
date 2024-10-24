import timeit

# ДИНАМІЧНЕ ПРОГРАМУВАННЯ
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Ініціалізуємо таблицю для мінімальної кількості монет для кожної суми від 0 до amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # 0 монет для суми 0

    # Таблиця для відстеження номіналів монет, які використовуються
    used_coins = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    # Відновлюємо результат — які монети були використані
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = used_coins[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result


print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
# print(find_min_coins(11300000))  # {50: 226000}

dp_time = timeit.timeit('find_min_coins(113)', globals=globals(), number=1000)
print("Час виконання динамічного програмування на 1000 прогонів:", dp_time, "секунд")
