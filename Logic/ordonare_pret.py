from Domain.Obiect import get_pret


def ordonare_dupa_pret(obiecte, undo_list, redo_list):
    """
    ordoneaza lista de obiecte in functie de pretul de achizitie
    :param undo_list:
    :param redo_list:
    :param obiecte:
    :return: returneaza lista obiectelor ordonata dupa pret
    """
    undo_list.append(obiecte)
    redo_list.clear()
    return sorted(obiecte, key=get_pret)
