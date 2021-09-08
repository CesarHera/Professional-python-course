def division_by(n: float):
    assert type(n) == float, 'Float expected'
    def divisor(m: float):
        assert type(m) == float, 'Float expected'
        return m / n
    return divisor

def run():
    print(division_by(3.0)(18.0))
    assert division_by(3.0)(18.0) == 18.0 / 3.0, 'Test 1 failed'

    print(division_by(5.0)(100.0))
    assert division_by(5.0)(100.0) == 100.0 / 5.0, 'Test 2 failed'

    print(division_by(18.0)(54.0))
    assert division_by(18.0)(54.0) == 54.0 / 18.0, 'Test 3 failed'

if __name__ == '__main__':
    run()