def division_by(n):
    assert type(n) == float, 'Float expected'
    def divisor(m):
        assert type(m) == float, 'Float expected'
        return str(m / n)
    return divisor

def run():
    division_by_3 = division_by(3.0)
    print(division_by_3(18.0))

    division_by_3 = division_by(5.0)
    print(division_by_3(100.0))

    division_by_3 = division_by(18.0)
    print(division_by_3(54.0))

if __name__ == '__main__':
    run()