def fibo_divisor_sum(limit, divisor):
    current_term = 0
    next_term = 1
    f_sum = 0
    while current_term < limit:
        current_term, next_term = next_term, current_term + next_term
        if current_term % divisor == 0:
            f_sum += current_term
    return f_sum


print(fibo_divisor_sum(4000000, 2))
