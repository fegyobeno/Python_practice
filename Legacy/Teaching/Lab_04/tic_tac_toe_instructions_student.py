# Hozz létre egy kilenc mezőből álló táblát
board = #TODO

# Rajzold ki a táblát egy lambda függvényel
# (method) def join(
#     iterable: Iterable[str],
#     /
# ) -> str
# A join össze konkatenál bárhány stringet egyetlen string-é úgy, hogy azt a stringet használja elválasztónak amire meghívtuk a joint
# '.'.join(['a', 'b', 'c']) -> 'a.b.c'
display_board = lambda #TODO:

# Nézd meg, hogy egy játékosnak össze jött-e a győzelem (3 egyforma jel egymás mellett, átlósan, sorban vagy oszlopban)
# any() visszatérít egy igaz értéket ha bármelyik elem igaz, egyébként hamis
# all() visszatérít egy igaz értéket ha minden elem igaz, egyébként hamis
check_win = lambda #TODO


# Nézds meg, hogy minden pozíción van-e már egy játékos, ha igen akkor döntetlen
check_draw = lambda #TODO

# Lépés megvalósítása -> helyezd el a játékos jelet a táblán
# (method) def __setitem__(self, key: int, value: str) -> None
# __setitem__ egy speciális metódus, amelye a [] operátort hívja meg
# [1,2,3].__setitem__(1, 4) -> [1,4,3]   
make_move = lambda #TODO

# Fő ciklus
# Rajzoljuk ki a táblát
# Kérjük be a játékos lépését
# Ellenőrizzük, hogy nyert-e valaki
# Ellenőrizzük, hogy döntetlen-e
def play_game():
    #TODO

play_game()