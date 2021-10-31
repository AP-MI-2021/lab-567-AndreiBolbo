from Domain.Obiect import creare_obiect, get_descriere
from Logic.concatenare import concatenare_string


def get_data():
    return [
        creare_obiect(1, 'imprimanta', 'desc1', 150, 'd314'),
        creare_obiect(2, 'scaun', 'desc2', 50, 'p312'),
        creare_obiect(3, 'laptop', 'desc3', 180, 'e3'),
        creare_obiect(4, 'proiector', 'desc4', 350, 'a367'),
        creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    ]


def test_concatenare():
    obiecte = get_data()
    string = 'sd'
    val = 100
    lst = concatenare_string(obiecte, string, val)
    assert get_descriere(obiecte[0]) != get_descriere(lst[0])
    assert  get_descriere(obiecte[2]) != get_descriere(lst[2])
