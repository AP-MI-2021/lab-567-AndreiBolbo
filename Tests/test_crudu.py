from Domain.Obiect import creare_obiect, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creare_obiect(1, 'imprimanta', 'desc1', 150, 'd314'),
        creare_obiect(2, 'scaun', 'desc2', 50, 'p312'),
        creare_obiect(3, 'laptop', 'desc3', 180, 'e332'),
        creare_obiect(4, 'proiector', 'desc4', 350, 'a367'),
        creare_obiect(5, 'oglinda', 'desc5', 100, 'b356')
    ]


def test_create():
    obiecte = get_data()
    params = (6, 'dulap', 'desc6', 35, 'e554')
    new_obiect = creare_obiect(*params)
    lst = create(obiecte, *params)
    assert new_obiect in lst


def test_read():
    obiecte = get_data()
    s_obiect = obiecte[2]
    assert read(obiecte, get_id(s_obiect)) == s_obiect


def test_update():
    obiecte = get_data()
    params = (5, 'dulap', 'desc6', 35, 'e554')
    up_obiect = creare_obiect(*params)
    lst = update(obiecte, up_obiect)
    assert up_obiect not in obiecte
    assert up_obiect in lst
    assert len(lst) == len(obiecte)


def test_delete():
    obiecte = get_data()
    de = 2
    obiect_del = read(obiecte, de)
    lst = delete(obiecte, de)
    assert len(lst)+1 == len(obiecte)
    assert obiect_del not in lst
    assert obiect_del in obiecte


def test():
    test_create()
    test_read()
    test_update()
    test_delete()
