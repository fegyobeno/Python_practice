# Initialize the board
board = [' ' for _ in range(9)]

# Display the board
# (method) def join(
#     iterable: Iterable[str],
#     /
# ) -> str
# A join össze konkatenál bárhány stringet egyetlen string-é úgy, hogy azt a stringet használja elválasztónak amire meghívtuk a joint
# '.'.join(['a', 'b', 'c']) -> 'a.b.c'
display_board = lambda: print('\n'.join([' | '.join(board[i:i+3]) for i in range(0, 9, 3)]))

# Nézze meg, hogy egy játékosnak össze jött-e a győzelem (3 egyforma jel egymás mellett, átlósan, sorban vagy oszlopban)
# any() visszatérít egy igaz értéket ha bármelyik elem igaz, egyébként hamis
# all() visszatérít egy igaz értéket ha minden elem igaz, egyébként hamis
check_win = lambda b, p: any(all(b[i] == p for i in line) for line in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)])


# Nézze meg, hogy minden pozíción van-e már egy játékos, ha igen akkor döntetlen
check_draw = lambda b: all(s != ' ' for s in b)

# Lépés megvalósítása
# (method) def __setitem__(self, key: int, value: str) -> None
# __setitem__ egy speciális metódus, amelye a [] operátort hívja meg
# [1,2,3].__setitem__(1, 4) -> [1,4,3]   
make_move = lambda b, p, pos: b.__setitem__(pos, p)

# Fő ciklus
# Rajzoljuk ki a táblát
# Kérjük be a játékos lépését
# Ellenőrizzük, hogy nyert-e valaki
# Ellenőrizzük, hogy döntetlen-e
def play_game():
    for i in range(9):
        display_board()
        player = 'X' if i % 2 == 0 else 'O'
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (0-8): "))
                if 0 <= move <= 8 and board[move] == ' ' :
                    break
                else:
                    if 0 >= move or move >= 8:
                        raise ValueError("Invalid move")
                    else:
                        raise ValueError("Your opponent already stepped there")
            except ValueError as e:
                print(e)
        make_move(board, player, move)
        if check_win(board, player):
            display_board()
            print(f"Player {player} wins!")
            return
        if check_draw(board):
            display_board()
            print("It's a draw!")
            return

play_game()