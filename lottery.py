from random import choice
lst = [i for i in range(1, 31)]
def stavka(lot, amount):
    win_lot = choice(lst)
    if lot == win_lot:
        print(f'Вы выиграли {amount*2}$ T_T')
        return amount * 2
    print(f'Вы проиграли {amount}$ :D')
    return -amount