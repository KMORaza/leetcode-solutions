from collections import defaultdict
from typing import List
class DirectoryNode:
    def __init__(self):
        self.kids = {}
        self.is_removed = False
class Solution:
    def deleteDuplicateFolder(self, file_paths: List[List[str]]) -> List[List[str]]:
        output = []
        structure_to_nodes_map = defaultdict(list)
        self.root_directory = DirectoryNode()
        file_paths.sort(key=lambda path: (path, len(path)))
        for path in file_paths:
            current_dir = self.root_directory
            for folder in path:
                if folder not in current_dir.kids:
                    current_dir.kids[folder] = DirectoryNode()
                current_dir = current_dir.kids[folder]
        self.map_structure_to_nodes(self.root_directory, structure_to_nodes_map)
        for node_list in structure_to_nodes_map.values():
            if len(node_list) > 1:
                for node in node_list:
                    node.is_removed = True
        self.create_output_paths(self.root_directory, [], output)
        return output
    def map_structure_to_nodes(self, node: DirectoryNode, structure_to_nodes_map: defaultdict):
        serialized_structure = ["("]
        for folder in sorted(node.kids.keys()):
            child_directory = node.kids[folder]
            serialized_structure.append(folder)
            serialized_structure.append(self.map_structure_to_nodes(child_directory, structure_to_nodes_map))
        serialized_structure.append(")")
        structure_representation = ''.join(serialized_structure)
        if structure_representation != "()":
            structure_to_nodes_map[structure_representation].append(node)
        return ''.join(serialized_structure)
    def create_output_paths(self, node: DirectoryNode, path_so_far: List[str], output: List[List[str]]):
        for folder in sorted(node.kids.keys()):
            child_directory = node.kids[folder]
            if not child_directory.is_removed:
                path_so_far.append(folder)
                self.create_output_paths(child_directory, path_so_far, output)
                path_so_far.pop()
        if path_so_far:
            output.append(path_so_far.copy())
