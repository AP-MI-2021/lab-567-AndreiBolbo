from Domain.Obiect import creare_obiect, get_str
from Logic.concatenare import concatenare_string
from Logic.crud import create, delete, update
from Logic.mutare import mutare_obiecte


def menu_help():
    print("Spre exemplu pentru comenzi din"
          "CRUD:add,id_obiect, nume, descriere, pret_achizitie, locatie")
    print("Pentru afisarea tuturor obiectelor :show_all")
    print("Pentru mutarea dintr-o locatie in alta a obiectelor:mutare,locatie_initiala,locatie_noua")
    print("Pentru concatenarea unui string la descriere a tuturor obiectelor "
          "cu pretul mai mare decat o valoare: concatenare,string,val")
    print("Iar pentru folosirea mai multor actiuni la o singura citire vom proceda astfel:add,id_obiect, nume, "
          "descriere, pret_achizitie, locatie;show_all;mutare,locatie_initiala,locatie_noua;"
          "concatenare,string,val")


def console(obiecte):
    while True:
        option = input("Dati sirul de actiuni/comenzi dorite sau scrieti 'Help' pentru ajutor sau "
                       "scrieti x pentru a iesi:")
        if option == 'Help':
            menu_help()
        if option == 'x':
            break
        else:
            comenzi = option.split(';')
            for elemente in comenzi:
                actiuni = elemente.split(',')
                if actiuni[0] == 'add':
                    try:
                        obiecte = create(obiecte, int(actiuni[1]), actiuni[2], actiuni[3], int(actiuni[4]), actiuni[5])
                    except ValueError as ve:
                        print("Eroare", ve)
                elif actiuni[0] == 'delete':
                    try:
                        obiecte = delete(obiecte, int(actiuni[1]))
                    except ValueError as ve:
                        print("Eroare", ve)
                elif actiuni[0] == 'update':
                    try:
                        obiect = creare_obiect(int(actiuni[1]), actiuni[2], actiuni[3], int(actiuni[4]), actiuni[5])
                        obiecte = update(obiecte, obiect)
                    except ValueError as ve:
                        print("Eroare", ve)
                elif actiuni[0] == 'mutare':
                    try:
                        obiecte = mutare_obiecte(obiecte, actiuni[1], actiuni[2])
                    except ValueError as ve:
                        print("Eroare", ve)
                elif actiuni[0] == 'concatenare':
                    try:
                        obiecte = concatenare_string(obiecte, actiuni[1], int(actiuni[2]))
                    except ValueError as ve:
                        print("Eroare", ve)
                elif actiuni[0] == 'show_all':
                    for obiect in obiecte:
                        print(get_str(obiect))
                else:
                    print("optiune gresita")
    return obiecte
