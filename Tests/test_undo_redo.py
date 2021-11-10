from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo


def testare():
    lst_obiecte = []
    undo_list = []
    redo_list = []
    lst_obiecte = create(lst_obiecte, 1, 'masa', 'desc', 150, 'erfs', undo_list, redo_list)
    lst_obiecte = create(lst_obiecte, 2, 'dulap', 'desc', 70, 'arfs', undo_list, redo_list)
    lst_obiecte = create(lst_obiecte, 3, 'sac', 'desc', 80, 'arss', undo_list, redo_list)
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 2
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 1
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 0
    assert do_undo(undo_list, redo_list, lst_obiecte) is None
    lst_obiecte = create(lst_obiecte, 1, 'masa', 'desc', 150, 'erfs', undo_list, redo_list)
    lst_obiecte = create(lst_obiecte, 2, 'dulap', 'desc', 70, 'arfs', undo_list, redo_list)
    lst_obiecte = create(lst_obiecte, 3, 'sac', 'desc', 80, 'arss', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, lst_obiecte) is None
    assert len(lst_obiecte) == 3
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 1
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 2
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 3
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 1
    lst_obiecte = create(lst_obiecte, 4, 'masa', 'desc', 150, 'erfs', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, lst_obiecte) is None
    assert len(lst_obiecte) == 2
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 1
    lst_obiecte = do_undo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 0
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    lst_obiecte = do_redo(undo_list, redo_list, lst_obiecte)
    assert len(lst_obiecte) == 2
    assert do_redo(undo_list, redo_list, lst_obiecte) is None

