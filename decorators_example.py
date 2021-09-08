def uppercase(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@uppercase
def greeting(name):
    return f'Hello {name}'

def run():
    print(greeting('name'))

if __name__ == '__main__':
    run()