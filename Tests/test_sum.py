from Domain.Obiect import creare_obiect
from Logic.sume_locatie import sume_pret_per_locatie


def get_data():
    return [
        creare_obiect(1, 'imprimanta', 'desc1', 150, 'p312'),
        creare_obiect(2, 'scaun', 'desc2', 50, 'p312'),
        creare_obiect(3, 'laptop', 'desc3', 180, 'e343'),
        creare_obiect(4, 'proiector', 'desc4', 350, 'a367'),
        creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    ]


def test_sum():
    obiecte = get_data()
    lst = sume_pret_per_locatie(obiecte)
    assert lst['p312'] == 200
    assert lst['e343'] == 180
