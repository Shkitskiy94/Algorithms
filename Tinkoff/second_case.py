results = []

def make_exchange_step(currency_value, currency_amounts, current_amounts):
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if current_amounts[i] < currency_value[i]:
                continue
            new_amounts = current_amounts
            new_amounts[i] -= currency_value[i]
            new_amounts[j] += currency_value[j]
            result = [new_amounts[0], new_amounts[1], new_amounts[2]]
            if result not in results:
                results.append(result)
                make_exchange_step(currency_value, currency_amounts, new_amounts)


def make_exchange(value, amounts):
    result = []
    result.append([amounts[0], amounts[1], amounts[2]])
    make_exchange_step(value, amounts, amounts)


if __name__ == '__main__':
    value = [int(n) for n in input().split(' ')]
    amounts = [int(n) for n in input().split(' ')]
    make_exchange(value, amounts)
    print(len(results) + 1)
