from Domain.Obiect import get_str, creare_obiect
from Logic.concatenare import concatenare_string
from Logic.crud import create, delete, update, read
from Logic.determinare_pret_per_locatie import determinare_pret_maxim_locatie
from Logic.mutare import mutare_obiecte
from Logic.ordonare_pret import ordonare_dupa_pret
from Logic.sume_locatie import sume_pret_per_locatie


def meniu():
    print("1. CRUD")
    print("2. Mutarea tuturor obiectelor dintr-o locatie in alta")
    print("3. Concatenarea unui string citit la toate descrierile obiectelor"
          " cu prețul mai mare decât o valoare citită.")
    print("4. Determinarea celui mai mare preț pentru fiecare locație.")
    print("5. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("6. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("7. Undo.")
    print("8. Redo.")
    print("x. Pentru a iesi din program")


def handle_add(obiecte):
    try:
        id_obiect = int(input("Dati id-ul:"))
        nume_obiect = input("Dati numele obiectului:")
        descriere_obiect = input("Dati descrierea obiectului:")
        pret_obiect = int(input("Dati pretul:"))
        locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
        return create(obiecte, id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
    except ValueError as ve:
        print('Eroare:', ve)
    return obiecte


def handle_del(obiecte):
    try:
        id_obiect = int(input("Dati id-ul elementului pe care vreti sa il stergeti:"))
        return delete(obiecte, id_obiect)
    except ValueError as ve:
        print('Eroare:', ve)
    return obiecte


def handle_up(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului pe care vreti sa il modificati:"))
        nume_obiect = input("Dati numele obiectului:")
        descriere_obiect = input("Dati descrierea obiectului:")
        pret_obiect = int(input("Dati pretul:"))
        locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
        obiect = creare_obiect(id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
        return update(obiecte, obiect)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_details(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului despre care vreti detalii:"))
        obiect = read(obiecte, id_obiect)
        return get_str(obiect)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_show_all(obiecte):
    for obiect in obiecte:
        print(get_str(obiect))


def handle_determinare(obiecte):
    lst = determinare_pret_maxim_locatie(obiecte)
    for locatie in lst:
        print(f'{locatie}: {get_str(lst[locatie])} ')


def handle_mutare(obiecte):
    try:
        locatie_initiala = input("Dati locatia din care sa se mute obiectele (4 caractere):")
        locatie_noua = input("Dati locatia in care sa se mute obiectele (4 caractere):")
        obiecte = mutare_obiecte(obiecte, locatie_initiala, locatie_noua)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_ordonare(obiecte):
    ordonate = ordonare_dupa_pret(obiecte)
    handle_show_all(ordonate)


def handle_new_list(obiecte, list_v, current_v):
    while current_v < len(list_v)-1:
        list_v.pop()
    list_v.append(obiecte)
    current_v += 1
    return list_v, current_v


def undo(list_v, current_v):
    if current_v == 0:
        print("Nu se mai poate face undo")
        return list_v[current_v], current_v
    else:
        current_v -= 1
        return list_v[current_v], current_v


def redo(list_v, current_v):
    if current_v == len(list_v)-1:
        print("Nu se mai poate face redo")
        return list_v[current_v], current_v
    else:
        current_v += 1
        return list_v[current_v], current_v


def meniu_crud(obiecte, list_v, current_v):
    while True:
        print("1. Adaugare obiect")
        print("2. Detalii obiect")
        print("3. Actualizare obiect")
        print("4. Stergere obiect")
        print("a. Afisare")
        print("b. Revenire")
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte = handle_add(obiecte)
            list_v, current_v = handle_new_list(obiecte, list_v, current_v)
        elif optiune == '2':
            print(handle_details(obiecte))
        elif optiune == '4':
            obiecte = handle_del(obiecte)
            list_v, current_v = handle_new_list(obiecte, list_v, current_v)
        elif optiune == '3':
            obiecte = handle_up(obiecte)
            list_v, current_v = handle_new_list(obiecte, list_v, current_v)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'b':
            break
        else:
            print("Optiune invalida")
    return obiecte, list_v, current_v


def handle_concatenare(obiecte):
    try:
        string = input("Dati string-ul de adaugat la descriere:")
        val = int(input("Dati valoarea de comparat cu pretul obiectelor:"))
        obiecte = concatenare_string(obiecte, string, val)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_sum(obiecte):
    lst = sume_pret_per_locatie(obiecte)
    for locatie in lst:
        print(f'{locatie} are suma preturilor {lst[locatie]}')


def run_ui(obiecte):
    list_v = [obiecte]
    current_v = 0
    while True:
        meniu()
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte, list_v, current_v = meniu_crud(obiecte, list_v, current_v)
        elif optiune == '2':
            obiecte = handle_mutare(obiecte)
            list_v, current_v = handle_new_list(obiecte, list_v, current_v)
        elif optiune == '3':
            obiecte = handle_concatenare(obiecte)
            list_v, current_v = handle_new_list(obiecte, list_v, current_v)
        elif optiune == '4':
            handle_determinare(obiecte)
        elif optiune == '5':
            handle_ordonare(obiecte)
        elif optiune == '6':
            handle_sum(obiecte)
        elif optiune == '7':
            obiecte, current_v = undo(list_v, current_v)
        elif optiune == '8':
            obiecte, current_v = redo(list_v, current_v)
        else:
            break
    return obiecte
