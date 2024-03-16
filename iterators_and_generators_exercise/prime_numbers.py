def get_primes(some_list):
    for num in some_list:
        if num < 2:
            continue
        counter = 2
        is_prime = True
        while counter < num:
            if num % counter == 0:
                is_prime = False
                break
            counter += 1
        if is_prime:
            yield num

