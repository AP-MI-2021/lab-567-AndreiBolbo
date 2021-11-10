from Domain.Obiect import creare_obiect, get_id


def create(lst_obiecte, id_obiect, nume, descriere, pret_achizitie, locatie, undo_list, redo_list):
    """

    :param lst_obiecte: lista de obiecte
    :param id_obiect:
    :param nume:
    :param descriere:
    :param pret_achizitie:
    :param locatie:
    :return:o noua lista de obiecte compusa din lista initiala si noul obiect
    """
    if read(lst_obiecte, id_obiect) is not None:
        raise ValueError(f'Exista deja un obiect cu id-ul {id_obiect}')
    if len(locatie) != 4:
        raise ValueError(f'locatie introdusa gresit ')
    undo_list.append(lst_obiecte)
    redo_list.clear()
    obiect = creare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
    return lst_obiecte+[obiect]


def read(lst_obiecte, id_obiect=None):
    """
    "Citeste" un obiect din lista (il cauta practic )
    :param lst_obiecte:
    :param id_obiect:
    :return:obiectul cu id-ul cerut sau toata lista in caz ca acesta nu exista
    """
    if not id_obiect:
        return lst_obiecte
    obiect_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_cu_id = obiect
    if obiect_cu_id:
        return obiect_cu_id
    return None


def update(lst_obiecte, obiect_1,  undo_list, redo_list):
    """
    Modifica un obiect
    :param lst_obiecte: lista de obiecte
    :param obiect_1: cu id existent
    :return: lista de obiecte modificata
    """
    if read(lst_obiecte, get_id(obiect_1)) is None:
        raise ValueError(f'Nu exista obiectul cu id-ul {get_id(obiect_1)} pe care sa il actualizam.')
    new_lst_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != get_id(obiect_1):
            new_lst_obiecte.append(obiect)
        else:
            new_lst_obiecte.append(obiect_1)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return new_lst_obiecte


def delete(lst_obiecte, id_obiect, undo_list, redo_list):
    if read(lst_obiecte, id_obiect) is None:
        raise ValueError(f'Nu exista obiectul cu id-ul {id_obiect} pe care sa il stergem.')
    new_lst_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != id_obiect:
            new_lst_obiecte.append(obiect)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return new_lst_obiecte
