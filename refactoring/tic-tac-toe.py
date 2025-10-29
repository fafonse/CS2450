import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show(b):  # Display board b
    for r in range(3):
        print(f" {b[r * 3]} | {b[r * 3 + 1]} | {b[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---")


def winner(b):  # Determine winner from board b
    if b[0] == b[1] == b[2]:  # straights
        return b[0]
    elif b[3] == b[4] == b[5]:
        return b[3]
    elif b[6] == b[7] == b[8]:
        return b[6]
    elif b[0] == b[3] == b[6]:  # diagonals
        return b[0]
    elif b[1] == b[4] == b[7]:
        return b[1]
    elif b[2] == b[5] == b[8]:
        return b[2]
    elif b[0] == b[4] == b[8]:
        return b[0]
    elif b[2] == b[4] == b[6]:
        return b[2]

    return None


def play():
    b = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in b):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(b)
        print(f"\n{turn}'s turn!")  # Attempt player turn
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and b[move].isdigit():
            b[move] = turn
            winner_result = winner(b)
            if winner_result:  # declare winner if found
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(b)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen()
    print("Tic-Tac-Toe\n")
    show(b)
    print("\nIt's a draw!")


play()
