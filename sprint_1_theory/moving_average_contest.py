def moving_average(list_data, K):
    result = []
    current_sum = sum(list_data[0:K])
    result.append(current_sum / K)
    for i in range(0, len(list_data) - K):
        current_sum -= list_data[i]
        current_sum += list_data[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


data = [9, 3, 2, 0, 1, 5, 1, 0, 0]
print(moving_average(data, 3))
