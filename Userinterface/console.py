from Domain.Obiect import get_str, creare_obiect
from Logic.concatenare import concatenare_string
from Logic.crud import create, delete, update, read
from Logic.determinare_pret_per_locatie import determinare_pret_maxim_locatie
from Logic.mutare import mutare_obiecte
from Logic.ordonare_pret import ordonare_dupa_pret
from Logic.sume_locatie import sume_pret_per_locatie
from Logic.undo_redo import do_undo, do_redo


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


def handle_add(obiecte, undo_list, redo_list):
    try:
        id_obiect = int(input("Dati id-ul:"))
        nume_obiect = input("Dati numele obiectului:")
        descriere_obiect = input("Dati descrierea obiectului:")
        pret_obiect = int(input("Dati pretul:"))
        locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
        return create(obiecte, id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect, undo_list,
                      redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    return obiecte


def handle_del(obiecte, undo_list, redo_list):
    try:
        id_obiect = int(input("Dati id-ul elementului pe care vreti sa il stergeti:"))
        return delete(obiecte, id_obiect, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    return obiecte


def handle_up(obiecte, undo_list, redo_list):
    try:
        id_obiect = int(input("Dati id-ul obiectului pe care vreti sa il modificati:"))
        nume_obiect = input("Dati numele obiectului:")
        descriere_obiect = input("Dati descrierea obiectului:")
        pret_obiect = int(input("Dati pretul:"))
        locatie_obiect = input("Dati locatia obiectului ,exact 4 caractere:")
        obiect = creare_obiect(id_obiect, nume_obiect, descriere_obiect, pret_obiect, locatie_obiect)
        return update(obiecte, obiect, undo_list, redo_list)
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


def handle_mutare(obiecte, undo_list, redo_list):
    try:
        locatie_initiala = input("Dati locatia din care sa se mute obiectele (4 caractere):")
        locatie_noua = input("Dati locatia in care sa se mute obiectele (4 caractere):")
        obiecte = mutare_obiecte(obiecte, locatie_initiala, locatie_noua, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_ordonare(obiecte, undo_list, redo_list):
    ordonate = ordonare_dupa_pret(obiecte, undo_list, redo_list)
    handle_show_all(ordonate)
    return ordonate


def meniu_crud(obiecte,  undo_list, redo_list):
    while True:
        print("1. Adaugare obiect")
        print("2. Detalii obiect")
        print("3. Actualizare obiect")
        print("4. Stergere obiect")
        print("a. Afisare")
        print("b. Revenire")
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte = handle_add(obiecte, undo_list, redo_list)
        elif optiune == '2':
            print(handle_details(obiecte))
        elif optiune == '4':
            obiecte = handle_del(obiecte, undo_list, redo_list)
        elif optiune == '3':
            obiecte = handle_up(obiecte,  undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'b':
            break
        else:
            print("Optiune invalida")
    return obiecte


def handle_concatenare(obiecte, undo_list, redo_list):
    try:
        string = input("Dati string-ul de adaugat la descriere:")
        val = int(input("Dati valoarea de comparat cu pretul obiectelor:"))
        obiecte = concatenare_string(obiecte, string, val,  undo_list, redo_list)
    except ValueError as ve:
        print("Eroare:", ve)
    return obiecte


def handle_sum(obiecte):
    lst = sume_pret_per_locatie(obiecte)
    for locatie in lst:
        print(f'{locatie} are suma preturilor {lst[locatie]}')


def handle_undo(obiecte, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, obiecte)
    if undo_result:
        return undo_result
    return obiecte


def handle_redo(obiecte, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, obiecte)
    if redo_result:
        return redo_result
    return obiecte


def run_ui(obiecte, undo_list, redo_list):
    while True:
        meniu()
        optiune = input("Alegeti optiunea dorita:")
        if optiune == '1':
            obiecte = meniu_crud(obiecte, undo_list, redo_list)
        elif optiune == '2':
            obiecte = handle_mutare(obiecte, undo_list, redo_list)

        elif optiune == '3':
            obiecte = handle_concatenare(obiecte, undo_list, redo_list)

        elif optiune == '4':
            handle_determinare(obiecte)
        elif optiune == '5':
            obiecte = handle_ordonare(obiecte, undo_list, redo_list)
        elif optiune == '6':
            handle_sum(obiecte)
        elif optiune == '7':
            obiecte = handle_undo(obiecte, undo_list, redo_list)
        elif optiune == '8':
            obiecte = handle_redo(obiecte, undo_list, redo_list)
        else:
            break
    return obiecte
