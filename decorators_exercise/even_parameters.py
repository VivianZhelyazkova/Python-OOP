def even_parameters(some_func):
    def wrapper(*args, **kwargs):
        even_parameters = [num for num in args if type(num) == int and num % 2 == 0]
        if len(args) == len(even_parameters):
            result = some_func(*args)
            return result
        else:
            return "Please use only even numbers!"
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))