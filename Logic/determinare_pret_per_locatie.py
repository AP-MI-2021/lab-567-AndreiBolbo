from Domain.Obiect import get_locatie, get_pret


def determinare_pret_maxim_locatie(lst_obiecte):
    """
    determina pretul maxim pentru fiecare locatie
    :param lst_obiecte:
    :return: lst- care e un dictionar in care cheia este locatia iar valoarea este obiectul complet
    """
    lst = {}
    for obiect in lst_obiecte:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie not in lst:
            lst[locatie] = obiect
        else:
            if pret > get_pret(lst[locatie]):
                lst[locatie] = obiect
    return lst
