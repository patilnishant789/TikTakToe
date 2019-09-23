list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def show():
    print(list[0], '|', list[1], '|', list[2])
    print('---------')
    print(list[3], '|', list[4], '|', list[5])
    print('---------')
    print(list[6], '|', list[7], '|', list[8])


def winner(char, num1, num2, num3):
    if list[num1] == char and list[num2] == char and list[num3] == char:
        return True


def check(char):
    if winner(char, 0, 1, 2):
        return True
    elif winner(char, 3, 4, 5):
        return True
    elif winner(char, 6, 7, 8):
        return True
    elif winner(char, 0, 3, 6):
        return True
    elif winner(char, 1, 4, 7):
        return True
    elif winner(char, 2, 5, 8):
        return True
    elif winner(char, 0, 4, 8):
        return True
    elif winner(char, 2, 4, 6):
        return True
    else:
        return False


show()
while True:
    print()
    player1 = int(input("Player1: "))
    print()

    if list[player1] != 'x' and list[player1] != 'o':
        list[player1] = 'x'
    else:
        print("This place is already taken.")
        print()
    show()
    if check('x'):
        print("~~ Player1 Winner ~~")
        break

    print()
    player2 = int(input("Player2: "))
    print()

    if list[player2] != 'x' and list[player2] != 'o':
        list[player2] = 'o'
    else:
        print("This place is already taken.")
        print()
    show()
    if check('o'):
        print("~~ Player2 Winner ~~")
        break
