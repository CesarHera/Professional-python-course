def prime_detector(number: int) -> bool:
    if number == 1:
        return False
    if number == 2:
        return True
    elif number < 1:
        return False

    for i in range(1, number):
        if i == 1:
            continue
        elif number % i == 0:
            return False
    return True


def run():
    print('Welcome to the prime finder list :)')
    range = int(input('Type the list limit: '))
    print([i for i in range(0, range + 1) if prime_detector(i)])


if __name__ == '__main__':
    run()