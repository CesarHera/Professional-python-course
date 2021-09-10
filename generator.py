def c_gen(max=None):
    n = 0
    while n ** 2 < max:
        yield n ** 2
        n += 1

this_gen = c_gen(10)
for item in this_gen:
    print(item)