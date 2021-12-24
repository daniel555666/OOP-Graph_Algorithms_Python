import src.gui.constants


def reset_add_node_string():
    src.gui.constants.user_text_add_node = 'add node'


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

