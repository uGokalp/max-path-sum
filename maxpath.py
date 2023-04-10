from typing import Dict

from models import Tree, TreeData


def parse_nodes(data: TreeData) -> Tree:
    """
    Parse nodes from TreeData and return root node

    :param data: TreeData
    :return: root Tree
    """
    nodes = data.tree.nodes
    root: str = data.tree.root
    node_map: Dict[str, Tree] = {}
    for node in nodes:
        node_id = node.id
        node_map[node_id] = Tree(value=node.value)
    for node in nodes:
        node_id = node.id
        current_node = node_map[node_id]
        left_child_id = node.left
        right_child_id = node.right
        if left_child_id:
            current_node.left = node_map[left_child_id]
        if right_child_id:
            current_node.right = node_map[right_child_id]
    root_node = node_map[root]
    return root_node


class MaxPathSum:
    def find_max_path_sum(self, root: Tree) -> int:
        self.max_path_sum = float("-inf")
        self.__find_max_path_sum(root)
        return self.max_path_sum

    def __find_max_path_sum(self, root: Tree) -> int:
        if root is None:
            return 0
        left_sum = max(self.__find_max_path_sum(root.left), 0)
        right_sum = max(self.__find_max_path_sum(root.right), 0)
        path_sum = left_sum + right_sum + root.value
        self.max_path_sum = max(self.max_path_sum, path_sum)
        return max(left_sum, right_sum) + root.value


class MaxPathService:
    def find_max_path_sum(self, data: TreeData) -> int:
        tree = parse_nodes(data)
        path_sum = MaxPathSum()
        return path_sum.find_max_path_sum(tree)
