from Domain.Obiect import get_descriere, creare_obiect, get_locatie
from Logic.mutare import mutare_obiecte


def get_data():
    return [
        creare_obiect(1, 'imprimanta', 'desc1', 150, 'd314'),
        creare_obiect(2, 'scaun', 'desc2', 50, 'p312'),
        creare_obiect(3, 'laptop', 'desc3', 180, 'e3'),
        creare_obiect(4, 'proiector', 'desc4', 350, 'a367'),
        creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    ]


def tester():
    obiecte = get_data()
    locatie_initiala = 'd314'
    locatie_noua = 'l321'
    lst = mutare_obiecte(obiecte, locatie_initiala, locatie_noua)
    assert get_locatie(obiecte[0]) != get_locatie(lst[0])
    locatie_initiala = 'l321'
    locatie_noua = 'd314'
    lst = mutare_obiecte(obiecte, locatie_initiala, locatie_noua)
    assert get_locatie(obiecte[0]) == get_locatie(lst[0])


def test1():
    tester()
