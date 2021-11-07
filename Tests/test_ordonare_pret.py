from Domain.Obiect import creare_obiect
from Logic.ordonare_pret import ordonare_dupa_pret


def get_data():
    return [
        creare_obiect(1, 'imprimanta', 'desc1', 150, 'p312'),
        creare_obiect(2, 'scaun', 'desc2', 50, 'p312'),
        creare_obiect(3, 'laptop', 'desc3', 180, 'e343'),
        creare_obiect(4, 'proiector', 'desc4', 350, 'a367'),
        creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    ]


def test_ord():
    obiecte = get_data()
    lst = ordonare_dupa_pret(obiecte)
    assert lst[0] == obiecte[1]
    assert lst[0] != obiecte[0]
    