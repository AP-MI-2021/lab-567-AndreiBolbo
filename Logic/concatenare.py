from Domain.Obiect import get_pret, get_descriere, creare_obiect, get_locatie, get_nume, get_id


def concatenare_string(lst_obiecte, string, val,  undo_list, redo_list):
    """
    Concateneaza un string anume pentru obiectele cu pretul mai mare decat o valoare
    :param redo_list:
    :param undo_list:
    :param lst_obiecte:
    :param string:
    :param val:
    :return: lista noua modificata
    """
    new_lst = []
    for obiect in lst_obiecte:
        if get_pret(obiect) > val:
            s = get_descriere(obiect)+string
            new_obiect = creare_obiect(get_id(obiect), get_nume(obiect),
                                       s, get_pret(obiect), get_locatie(obiect))
            new_lst.append(new_obiect)
        else:
            new_lst.append(obiect)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return new_lst
