from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        return print("I took " + str(time_elapsed.total_seconds()) + " seconds on execution")
    return wrapper

@execution_time
def go_through_a_list():
    for _ in range(1_000_000_000):
        pass

def run():
    go_through_a_list()

if __name__ == '__main__':
    run()