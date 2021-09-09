import os
for hora in range(0, 24):
    os.system('cls')
    print(f'{hora}:00:00')
    for minuto in range(0, 60):
        os.system('cls')
        print(f'{hora}:{minuto}:00')
        for segundo in range(0, 60):
            os.system('cls')
            print(f'{hora}:{minuto}:{segundo}')