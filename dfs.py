from collections import deque

class HTMLGraphSearchDFS:
    def __init__(self, graph, content_dict):
        self.graph = graph
        self.content_dict = content_dict

    def dfs(self, start_node):
        visited = set()
        content_list = []
        self._dfs_recursive(start_node, visited, content_list)
        return content_list

    def _dfs_recursive(self, node, visited, content_list):
        if node not in visited:
            content_list.append(self.content_dict.get(node, ""))
            visited.add(node)
            for child in self.graph.get(node, []):
                self._dfs_recursive(child, visited, content_list)
