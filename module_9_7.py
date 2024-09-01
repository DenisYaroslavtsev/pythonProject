def is_prime(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        for i in range(2, int(result_func ** 0.5) + 1):
            if result_func % i == 0:
                print("Составное")
                return result_func
        print("Простое")
        return result_func

    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)