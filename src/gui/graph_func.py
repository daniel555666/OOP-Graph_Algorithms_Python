import src.gui.constants


def reset_add_node_string():
    src.gui.constants.user_text_add_node = 'add node'


def reset_remove_node_string():
    src.gui.constants.user_text_remove_node = 'remove node'

def reset_remove_edge_string():
    src.gui.constants.user_text_remove_edge = 'remove edge'


def add_node_g(user_text_add_node):
    split_str = user_text_add_node.split(",")
    if len(split_str) == 3:
        x = float(split_str[1])
        y = float(split_str[2])
        pos = (x, y, 0.0)
        node_id = int(split_str[0])
        value = src.gui.constants.ga.get_graph().add_node(node_id, pos)
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return value
    elif len(split_str) == 1:
        value = src.gui.constants.ga.get_graph().add_node(int(split_str[0]))
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return value


def remove_node_g(user_text_remove_node):
    input_str = user_text_remove_node
    if input_str.isnumeric():
        node_id = int(input_str)
        value = src.gui.constants.ga.get_graph().remove_node(node_id)
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return value
    else:
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return False


def remove_edge_g(user_text_remove_edge):
    input_str = user_text_remove_edge.split(",")
    if len(input_str) == 2:
        src_id = int(input_str[0])
        dest_id = int(input_str[1])
        value = src.gui.constants.ga.get_graph().remove_edge(src_id, dest_id)
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return value
    else:
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return False
