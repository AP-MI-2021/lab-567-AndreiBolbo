

def creare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie):
    """
    creeaza un obiect
    :param id_obiect: -unic
    :param nume: -numele obiectului
    :param descriere:-descrierea obiectului
    :param pret_achizitie:-pretul cu care s-a cumparat
    :param locatie:-locatia unde este obiectul
    :return: un obiect
    """
    return {
        'id': id_obiect,
        'nume': nume,
        'desc': descriere,
        'pret': pret_achizitie,
        'loc': locatie
    }


def get_id(obiect):
    """
    getter pentru id obiect
    :param obiect: obiectul
    :return: id-ul obiectului dat ca parametru
    """
    return obiect['id']


def get_nume(obiect):
    """
    getter pentru nume obiect
    :param obiect: obiectul
    :return: numele obiectului dat ca parametru
    """
    return obiect['nume']


def get_descriere(obiect):
    """
    getter pentru descriere obiect
    :param obiect: obiectul
    :return: descrierea obiectului dat ca parametru
    """
    return obiect['desc']


def get_pret(obiect):
    """
    getter pentru pret obiect
    :param obiect: obiectul
    :return: pretul obiectului dat ca parametru
    """
    return obiect['pret']


def get_locatie(obiect):
    """
    getter pentru locatie obiect
    :param obiect: obiectul
    :return: locatia obiectului dat ca parametru
    """
    return obiect['loc']


def get_str(obiect):
    """

    :param obiect:
    :return: reprezentarea obiectului ca string
    """
    return f'Obiectul cu id-ul {get_id(obiect)} este :{get_nume(obiect)} ,{get_descriere(obiect)} , ' \
           f'a costat {get_pret(obiect)} ' \
           f'si se afla in {get_locatie(obiect)}'
