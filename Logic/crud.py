from Domain.Obiect import creare_obiect, get_id


def create(lst_obiecte, id_obiect, nume, descriere, pret_achizitie, locatie):
    """

    :param lst_obiecte: lista de obiecte
    :param id_obiect:
    :param nume:
    :param descriere:
    :param pret_achizitie:
    :param locatie:
    :return:o noua lista de obiecte compusa din lista initiala si noul obiect
    """
    obiect = creare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
    return lst_obiecte+[obiect]


def read(lst_obiecte, id_obiect=None):
    """
    "Citeste" un obiect din lista (il cauta practic )
    :param lst_obiecte:
    :param id_obiect:
    :return:obiectul cu id-ul cerut sau toata lista in caz ca acesta nu exista
    """
    obiect_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_cu_id = obiect
    if obiect_cu_id:
        return obiect_cu_id
    return lst_obiecte


def update(lst_obiecte, obiect_1):
    """
    Modifica un obiect
    :param lst_obiecte: lista de obiecte
    :param obiect: cu id existent
    :return: lista de obiecte modificata
    """
    new_lst_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != get_id(obiect_1):
            new_lst_obiecte.append(obiect)
        else:
            new_lst_obiecte.append(obiect_1)
    return new_lst_obiecte


def delete(lst_obiecte, id_obiect):
    new_lst_obiecte=[]
    for obiect in lst_obiecte:
        if get_id(obiect) != id_obiect:
            new_lst_obiecte.append(obiect)
    return new_lst_obiecte