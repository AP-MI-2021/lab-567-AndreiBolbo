from Domain.Obiect import get_locatie, creare_obiect, get_id, get_nume, get_descriere, get_pret


def mutare_obiecte(lst_obiecte, locatie_initiala, locatie_noua, undo_list, redo_list):
    """
    Muta obiectele din locatia initiala in locatia noua
    :param redo_list:
    :param undo_list:
    :param lst_obiecte:
    :param locatie_initiala:
    :param locatie_noua:
    :return: lista cu obiectele mutate sau lista initiala daca locatia initiala nu exista
    """
    if len(locatie_noua) != 4 or len(locatie_initiala) != 4:
        raise ValueError(f'locatie introdusa gresit (trebuie de 4 caractere')
    new_lst = []
    for obiect in lst_obiecte:
        if get_locatie(obiect) == locatie_initiala:
            new_obiect = creare_obiect(get_id(obiect), get_nume(obiect),
                                       get_descriere(obiect), get_pret(obiect), locatie_noua)
            new_lst.append(new_obiect)
        else:
            new_lst.append(obiect)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return new_lst
