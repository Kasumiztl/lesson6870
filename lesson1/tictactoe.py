import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # рядки
            return True
        if all([board[j][i] == player for j in range(3)]):  # стовпці
            return True
    if all([board[i][i] == player for i in range(3)]):  # головна діагональ
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # побічна діагональ
        return True
    return False

def is_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                moves.append((i, j))
    return moves

def computer_move(board):
    moves = get_available_moves(board)
    return random.choice(moves)

def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    human = "X"
    computer = "O"

    while True:
        print_board(board)
        move = input("Твій хід (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Некоректне введення. Спробуй ще раз.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] in ['X', 'O']:
            print("Ця клітинка вже зайнята. Обери іншу.")
            continue

        board[row][col] = human

        if check_winner(board, human):
            print_board(board)
            print("Ти переміг!")
            break

        if is_draw(board):
            print_board(board)
            print("Нічия!")
            break

        # Хід комп'ютера
        row, col = computer_move(board)
        board[row][col] = computer
        print(f"\nКомп'ютер вибрав клітинку: {row * 3 + col + 1}")

        if check_winner(board, computer):
            print_board(board)
            print("Комп'ютер переміг!")
            break

        if is_draw(board):
            print_board(board)
            print("Нічия!")
            break

# Запуск гри
tic_tac_toe()