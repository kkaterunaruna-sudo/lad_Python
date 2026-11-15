def make_power(exponent):
    def power(base):
        return base ** exponent
    return power
power = make_power(5)
print(power(6))


def make_counter(start=0):
    count = start
    def increment(step = 1):
        nonlocal count
        count +=step
        return count
    return increment
counter = make_counter(10)
print(counter())
print(counter(5))
