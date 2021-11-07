from Domain.Obiect import get_locatie, get_pret


def sume_pret_per_locatie(lst_obiecte):
    """
    determina suma preturilor pentru fiecare locatie
    :param lst_obiecte:
    :return: un dictionar unde cheia este locatia iar valoarea este suma preturilor
    """
    lst = {}
    for obiect in lst_obiecte:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie not in lst:
            lst[locatie] = pret
        else:
            lst[locatie] += pret
    return lst
