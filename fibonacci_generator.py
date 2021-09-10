import time

# def fibonacci_gen(max=None):
#     n1 = 0
#     n2 = 1
#     counter = 0
#     while True:
#         if counter == 0:
#             counter += 1
#             yield f'Fibonacci número {counter}: {n1}'
#         elif counter == 1:
#             counter += 1
#             yield f'Fibonacci número {counter}: {n2}'
#         else:
#             if not max or counter + 1 <= max:
#                 counter += 1
#                 n1, n2 = n2, n1 + n2
#                 yield f'Fibonacci número {counter}: {n2}'
#             else:
#                 break

# fibonacci = fibonacci_gen()

# for n in fibonacci:
#     print(n)
#     time.sleep(0.001)


def gen(max: int = None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if not max or counter + 1 <= max:
            yield n1
            n1, n2 = n2, n1 + n2
            counter += 1
        else:
            break

fibonacci = gen(10)
for i in fibonacci:
    print(i)
    time.sleep(0.001)