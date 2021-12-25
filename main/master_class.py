import random 

while True:
    player = int(input("1 - камень, 2 - ножницы, 3- бумага"))
    if player == 1:
        print("игрок выбрал камень")
    if player == 2:
        print("игрок выбрал ножницы")
    if player == 3:
        print("игрок выбрал бумагу")

    computer = random.randint(1, 3)

    if computer == 1:
        print("computer выбрал камень")
    if computer == 2:
        print("computer выбрал ножницы")
    if computer == 3:
        print("computer выбрал бумагу")

    if player == computer:
        win=0
    if player == 1 and computer == 2:
        win = 1
    if player == 1 and computer == 3:
        win = 2
    if player == 2 and computer == 1:
        win = 2
    if player == 2 and computer == 3:
        win = 1
    if player == 3 and computer == 1:
        win = 1
    if player == 3 and computer == 2:
        win = 2

    if win == 0:
        print("Ничья!")
    elif win == 1:
        print("Игрок побеждает!")
    else:
        print("Компьютер победил!")
    