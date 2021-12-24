import src.gui.constants
from src.gui.draw_arrow import draw_arrow


def reset_add_node_string():
    src.gui.constants.user_text_add_node = 'add node'


def reset_remove_node_string():
    src.gui.constants.user_text_remove_node = 'remove node'


def reset_remove_edge_string():
    src.gui.constants.user_text_remove_edge = 'remove edge'


def reset_add_edge_string():
    src.gui.constants.user_text_add_edge = 'add edge'

def reset_node_loc_string():
    src.gui.constants.user_text_node_loc = 'hide location'

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


def add_edge_g(user_text_add_edge):
    input_str = user_text_add_edge.split(",")
    if len(input_str) == 3:
        src_id = int(input_str[0])
        dest_id = int(input_str[1])
        weight = float(input_str[2])
        value = src.gui.constants.ga.get_graph().add_edge(src_id, dest_id, weight)
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return value
    else:
        src.gui.constants.getminmax()
        src.gui.constants.calculate_values()
        return False


def node_loc_g():
    g = src.gui.constants.ga.get_graph()
    src.gui.constants.node_list.clear()
    src.gui.constants.src_edge_list.clear()
    src.gui.constants.dest_edge_list.clear()
    src.gui.constants.arrow_head_list.clear()
    for node in g.get_all_v().values():
        n_id = node.id
        x = (node.x - src.gui.constants.minX) * src.gui.constants.factorX + src.gui.constants.incrementX
        y = (node.y - src.gui.constants.minY) * src.gui.constants.factorY + src.gui.constants.incrementY
        src.gui.constants.node_list.append([x, y, n_id, node.x, node.y])

    for edge in src.gui.constants.ga.graph.Edges.values():
        x1 = src.gui.constants.incrementX + (
                g.get_all_v().get(edge.src).x - src.gui.constants.minX) * src.gui.constants.factorX
        y1 = src.gui.constants.incrementY + (
                g.get_all_v().get(edge.src).y - src.gui.constants.minY) * src.gui.constants.factorY
        x2 = src.gui.constants.incrementX + (
                g.get_all_v().get(edge.dest).x - src.gui.constants.minX) * src.gui.constants.factorX
        y2 = src.gui.constants.incrementY + (
                g.get_all_v().get(edge.dest).y - src.gui.constants.minY) * src.gui.constants.factorY
        if x1 > x2:
            y1 = y1 - 5
            y2 = y2 - 5
        else:
            y1 = y1 + 5
            y2 = y2 + 5
        src.gui.constants.src_edge_list.append([x1, y1])
        src.gui.constants.dest_edge_list.append([x2, y2])
        src.gui.constants.arrow_head_list.append(draw_arrow(x1, y1, x2, y2))
