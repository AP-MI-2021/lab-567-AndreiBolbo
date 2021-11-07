from Domain.Obiect import get_pret


def ordonare_dupa_pret(obiecte):
    """
    ordoneaza lista de obiecte in functie de pretul de achizitie
    :param obiecte:
    :return: returneaza lista obiectelor ordonata dupa pret
    """
    return sorted(obiecte, key=get_pret)
