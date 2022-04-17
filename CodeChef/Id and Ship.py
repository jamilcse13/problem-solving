def idAndShip():

    for _ in range(int(input())):
        n = input()
        char = n.lower()
        if char == 'b':
            print('BattleShip')
        elif char == 'c':
            print('Cruiser')
        elif char == 'd':
            print('Destroyer')
        elif char == 'f':
            print('Frigate')

if __name__ == "__main__":
    idAndShip()