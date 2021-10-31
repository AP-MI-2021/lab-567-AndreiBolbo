from Domain.Obiect import get_pret, get_descriere, creare_obiect, get_locatie, get_nume, get_id


def concatenare_string(lst_obiecte, string, val):
    new_lst = []
    for obiect in lst_obiecte:
        if get_pret(obiect)>val:
            s=get_descriere(obiect)+string
            new_obiect = creare_obiect(get_id(obiect), get_nume(obiect),
                                       s, get_pret(obiect), get_locatie(obiect))
            new_lst.append(new_obiect)
        else:
            new_lst.append(obiect)
    return new_lst
