# from Domain.obiect3 import creare_obiect
from Logic.crud import create
from Tests.test_crudu import test
from Tests.test_determinare_pret import tester
from Tests.test_mutare import test1
from Tests.test_ordonare_pret import test_ord
from Tests.test_sum import test_sum
from Tests.test_undo_redo import testare
from Userinterface.console import run_ui
# from Userinterface.consolecmd import console


def main():
    obiecte = []
    undo_list = []
    redo_list = []
    obiecte = create(obiecte, 1, 'imprimanta', 'desc1', 150, 'p312', undo_list, redo_list)
    obiecte = create(obiecte, 2, 'scaun', 'desc2', 50, 'p312', undo_list, redo_list)
    obiecte = create(obiecte, 3, 'laptop', 'desc3', 180, 'e3ds', undo_list, redo_list)
    obiecte = create(obiecte, 4, 'proiector', 'desc4', 350, 'a367', undo_list, redo_list)
    obiecte = create(obiecte, 5, 'oglinda', 'desc5', 100, 'b356', undo_list, redo_list)
    # obiect=creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    # print(obiect[2])
    # print(lst_a[0][0][1])
    # print("1. Pentru meniu vechi")
    # print("2. Pentru meniu nou cmd")
    # optiune = input("Alegeti tipul de meniu pe care vreti sa il folositi:")
    # if optiune == '1':
    run_ui(obiecte, undo_list, redo_list)
    # else:
    # obiecte = console(obiecte)


if __name__ == '__main__':
    testare()
    test_sum()
    test_ord()
    tester()
    test()
    test1()
    main()
