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
        1: id_obiect,
        2: nume,
        3: descriere,
        4: pret_achizitie,
        5: locatie
    }
