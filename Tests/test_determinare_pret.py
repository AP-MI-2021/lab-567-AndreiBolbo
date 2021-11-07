from Domain.Obiect import creare_obiect
from Logic.determinare_pret_per_locatie import determinare_pret_maxim_locatie


def get_data():
    return [
        creare_obiect(1, 'imprimanta', 'desc1', 150, 'p312'),
        creare_obiect(2, 'scaun', 'desc2', 50, 'p312'),
        creare_obiect(3, 'laptop', 'desc3', 180, 'e343'),
        creare_obiect(4, 'proiector', 'desc4', 350, 'a367'),
        creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    ]


def tester():
    obiecte = get_data()
    lst1 = determinare_pret_maxim_locatie(obiecte)
    assert lst1['p312'] == obiecte[0]
    assert lst1['e343'] == obiecte[2]