def test_return_type(expected_type):
    def tested_func(func):
        def wrapper(*args, **kwargs):
            if type(func(*args, **kwargs)) == expected_type:
                print
                return True
            else:
                return False
        return wrapper
    return tested_func


@test_return_type(int)
def square(n):
    return n ** 2

@test_return_type(str)
def remove_accent_marks(str):
    return str.translate(str.maketrans('ÁÉÍÓÚáéíóú', 'AEIOUaeiou'))

def run():
    print(square(4)) # Output: True
    print(remove_accent_marks('Ádiós')) # Output: True

if __name__ == '__main__':
    run()