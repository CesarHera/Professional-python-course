def tipo_encantamiento(tipo):
    def objeto_encantado(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'Reforzada con un poderoso encantamiento de tipo {tipo}')
        return wrapper
    return objeto_encantado

@tipo_encantamiento('Fuego')
def arma(fp):
    print(f'Tienes {fp} de fp')
    print('Espada de cola de dragón')

def run():
    arma(100)

if __name__ == '__main__':
    run()