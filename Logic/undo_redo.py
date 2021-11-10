def do_undo(undo_list, redo_list, current_list):
    """
    Sterge ultima operatiune facuta
    :param current_list:
    :param undo_list:
    :param redo_list: 
    :return: lista fara ultima operatiune/none
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo
    return None


def do_redo(undo_list, redo_list, current_list):
    """
    Revine la operatiunea dinainte de undo
    :param current_list:
    :param undo_list:
    :param redo_list:
    :return: lista de dinainte cu o operatiune in plus/none
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    return None
