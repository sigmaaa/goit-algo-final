import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def generate_color(step, total_steps):
    """ Генерує колір в форматі RGB, змінюючи відтінки в залежності від порядку обходу """
    intensity = int((step / total_steps) *
                    255)
    return f'#{intensity:02X}{0:02X}{255 - intensity:02X}'


def dfs(node, visit_order, color_map):
    if node is not None:
        color_map[node.id] = generate_color(len(visit_order), len(
            visit_order) + 1)  # Задати колір для вузла
        visit_order.append(node)
        dfs(node.left, visit_order, color_map)
        dfs(node.right, visit_order, color_map)


def bfs(root):
    visit_order = []
    queue = [root]
    color_map = {}

    while queue:
        node = queue.pop(0)
        if node is not None:
            color_map[node.id] = generate_color(len(visit_order), len(
                visit_order) + 1)  # Задати колір для вузла
            visit_order.append(node)
            queue.append(node.left)
            queue.append(node.right)

    return visit_order, color_map


def build_tree_from_heap(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


values = [10, 4, 3, 5, 8, 6]
min_heap = []
for value in values:
    heapq.heappush(min_heap, value)
min_heap_tree_root = build_tree_from_heap(min_heap)
draw_tree(min_heap_tree_root)
# Відображення бінарного дерева перед обходами
print("DFS Traversal:")
dfs_visit_order, dfs_color_map = [], {}
dfs(min_heap_tree_root, dfs_visit_order, dfs_color_map)
for node in dfs_visit_order:
    node.color = dfs_color_map[node.id]  # Встановлюємо колір для DFS обходу

draw_tree(min_heap_tree_root)

# Відображення бінарного дерева після DFS
print("BFS Traversal:")
bfs_visit_order, bfs_color_map = bfs(min_heap_tree_root)
for node in bfs_visit_order:
    node.color = bfs_color_map[node.id]  # Встановлюємо колір для BFS обходу

draw_tree(min_heap_tree_root)
