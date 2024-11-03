import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node[0], '#FFFFFF')
                   for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label']
              for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=node_colors)
    plt.title("Binary Tree with Traversal Visualization")
    plt.show()


def generate_color(step, total_steps):
    """ Generate color in RGB format, changing shades based on traversal order """
    intensity = int((step / total_steps) *
                    255)  # Color intensity from 0 to 255
    # Change color from blue to red
    return f'#{intensity:02X}{0:02X}{255 - intensity:02X}'


def dfs_iterative(root):
    """ Depth-first traversal using stack (iteratively) """
    visit_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node is not None:
            visit_order.append(node)
            stack.append(node.right)
            stack.append(node.left)

    return visit_order


def bfs_iterative(root):
    """ Breadth-first traversal using queue (iteratively) """
    visit_order = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node is not None:
            visit_order.append(node)
            queue.append(node.left)
            queue.append(node.right)

    return visit_order


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


if __name__ == "__main__":
    values = [10, 4, 3, 5, 8, 6]
    min_heap = []
    for value in values:
        heapq.heappush(min_heap, value)

    root = build_tree_from_heap(min_heap)

    print("DFS Traversal:")
    dfs_visit_order = dfs_iterative(root)
    dfs_colors = {}
    for step, node in enumerate(dfs_visit_order):
        dfs_colors[node.id] = generate_color(
            step, len(dfs_visit_order))

    draw_tree(root, dfs_colors)

    print("BFS Traversal:")
    bfs_visit_order = bfs_iterative(root)
    bfs_colors = {}
    for step, node in enumerate(bfs_visit_order):
        bfs_colors[node.id] = generate_color(
            step, len(bfs_visit_order))

    draw_tree(root, bfs_colors)
