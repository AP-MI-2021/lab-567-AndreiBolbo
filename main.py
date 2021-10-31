from Logic.crud import create
from Tests.test_crudu import test
from Tests.test_mutare import test1
from Userinterface.console import run_ui


def main():
    obiecte = []
    obiecte = create(obiecte, 1, 'imprimanta', 'desc1', 150, 'p312')
    obiecte = create(obiecte, 2, 'scaun', 'desc2', 50, 'p312')
    obiecte = create(obiecte, 3, 'laptop', 'desc3', 180, 'e3ds')
    obiecte = create(obiecte, 4, 'proiector', 'desc4', 350, 'a367')
    obiecte = create(obiecte, 5, 'oglinda', 'desc5', 100, 'b356')
    # print(lst_a[0][0][1])
    obiecte = run_ui(obiecte)


if __name__ == '__main__':
    test()
    test1()
    main()
